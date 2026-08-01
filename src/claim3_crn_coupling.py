"""Finite CRN coupling audit for the active-U-statistic CLT proof route.

Theorem 2.4 invokes the Appendix CRN construction: the oracle and learned
sampling decisions use the same U_i~Uniform(0,1), with pi_hat converging to
pi_star at O(n^-1/2).  This script tests the directly measurable consequence
of Lemma HT-plugin-correct in a bounded two-stratum HT functional:

  sqrt(n) [T_n(pi_hat)-T_n(pi_star)] -> 0.

It is a finite Monte-Carlo audit of the coupling mechanism, not a proof of the
paper's full U-statistic CLT or confidence-interval coverage theorem.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

SEED = 20260801
SIZES = (200, 800, 3200)
REPLICATES = 2500
# Bounded, strictly interior oracle probabilities indexed by X in {0,1}.
P0, P1 = 0.35, 0.65


def one_scale(n: int, adaptive: bool, seed: int) -> dict:
    rng = np.random.default_rng(seed)
    # H2 case: sup |pi_hat-pi_star| = 0.10/sqrt(n).  The control deliberately
    # violates H2 with a fixed 0.10 discrepancy while retaining positivity.
    delta = 0.10 / np.sqrt(n) if adaptive else 0.10
    values = np.empty(REPLICATES)
    mismatch_rates = np.empty(REPLICATES)
    for repeat in range(REPLICATES):
        x = rng.integers(0, 2, size=n)
        # A bounded measurable omega with finite second moment as in Lemma 1.
        omega = 1.0 + x.astype(float)
        pi_star = np.where(x == 0, P0, P1)
        pi_hat = np.clip(pi_star + np.where(x == 0, delta, -delta), 0.01, 0.99)
        # The shared U is the CRN coupling.  Independent uniforms would not
        # test the source lemma's construction.
        uniforms = rng.random(n)
        xi_star = uniforms <= pi_star
        xi_hat = uniforms <= pi_hat
        t_star = np.mean(omega * xi_star / pi_star)
        t_hat = np.mean(omega * xi_hat / pi_hat)
        values[repeat] = np.sqrt(n) * (t_hat - t_star)
        mismatch_rates[repeat] = np.mean(xi_star != xi_hat)
    return {
        "n": n,
        "delta_sup": float(delta),
        "rms_sqrt_n_difference": float(np.sqrt(np.mean(values**2))),
        "mean_sqrt_n_difference": float(np.mean(values)),
        "mean_crn_mismatch_rate": float(np.mean(mismatch_rates)),
        "pi_star_range": [P0, P1],
        "pi_hat_range": [float(P0 - delta), float(P1 + delta)],
    }


def calculate() -> dict:
    adaptive = [one_scale(n, True, SEED + n) for n in SIZES]
    control = [one_scale(n, False, SEED + 10_000 + n) for n in SIZES]
    # The scaled CRN difference should shrink under the H2 rate; it should not
    # shrink to zero when H2 is violated by a fixed policy error.
    return {
        "seed": SEED,
        "replicates": REPLICATES,
        "functional": "T_n(pi)=n^-1 sum omega_i xi_i(pi)/pi_i(pi)",
        "source_scope": {
            "theorem": "Theorem 2.4 / Appendix Lemma HT-plugin-correct",
            "source_conditions": "H1 positivity and H2 sup-norm O_p(n^-1/2) learned-policy consistency",
            "crn": "same uniforms define xi_hat and xi_star",
        },
        "h2_satisfying_crn_results": adaptive,
        "fixed_error_h2_violation_negative_control": control,
        "adaptive_rms_decreases": adaptive[-1]["rms_sqrt_n_difference"] < adaptive[0]["rms_sqrt_n_difference"],
        "control_rms_not_small_at_largest_n": control[-1]["rms_sqrt_n_difference"] > 0.05,
    }


def main() -> None:
    print(json.dumps(calculate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
