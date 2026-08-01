"""Finite audit of the Theorem-2.2 optimal sampling-score mechanism.

The source theorem minimizes the leading sampling-dependent term
E[s(X)(1/pi(X)-1)] subject to a label budget, where
s(x)=E[(h1(Y)-h1_mu(mu(X)))^2 | X=x].  Constants and the -E[s(X)]
term do not affect the minimizer, so this script minimizes sum_x p_x s_x/pi_x.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path


# Three equally common covariate strata.  Each tuple is (label, probability).
# The prediction errors deliberately do not have the same ordering as the
# Hoeffding-projection residual uncertainties.
STRATA = [
    [(0.0, 0.75), (4.0, 0.25)],
    [(0.0, 0.50), (2.0, 0.50)],
    [(1.0, 0.80), (3.0, 0.20)],
]
PREDICTIONS = [0.4, 1.8, 2.8]
BUDGET = 1.5  # expected labels among the three equally weighted strata


def kernel(a: float, b: float) -> float:
    """Gini U-statistic kernel."""
    return abs(a - b)


def h1(value: float, distribution: list[tuple[float, float]]) -> float:
    return sum(probability * kernel(value, other) for other, probability in distribution)


def calculate() -> dict:
    px = [1.0 / len(STRATA)] * len(STRATA)
    y_distribution: list[tuple[float, float]] = []
    for mass, stratum in zip(px, STRATA):
        y_distribution.extend((value, mass * probability) for value, probability in stratum)
    mu_distribution = list(zip(PREDICTIONS, px))

    projection_scores = []
    raw_mse = []
    for prediction, stratum in zip(PREDICTIONS, STRATA):
        projected_prediction = h1(prediction, mu_distribution)
        projection_scores.append(
            sum(
                probability * (h1(value, y_distribution) - projected_prediction) ** 2
                for value, probability in stratum
            )
        )
        raw_mse.append(sum(probability * (value - prediction) ** 2 for value, probability in stratum))

    def allocate(scores: list[float]) -> list[float]:
        # All scores are positive and the returned values are below one, so the
        # source theorem's min{1, ...} clipping is inactive in this audit.
        scale = BUDGET / sum(score**0.5 for score in scores)
        return [scale * score**0.5 for score in scores]

    optimal_pi = allocate(projection_scores)
    raw_residual_pi = allocate(raw_mse)
    uniform_pi = [BUDGET / len(STRATA)] * len(STRATA)

    def leading_objective(pi: list[float]) -> float:
        return sum(mass * score / probability for mass, score, probability in zip(px, projection_scores, pi))

    # Independent finite grid check: values on 0.01 increments, preserving the
    # exact label budget. It is intentionally independent of the closed form.
    grid_best = (float("inf"), None)
    for a, b in itertools.product(range(1, 100), repeat=2):
        c = int(round(BUDGET * 100)) - a - b
        if not 1 <= c <= 99:
            continue
        candidate = [a / 100, b / 100, c / 100]
        value = leading_objective(candidate)
        if value < grid_best[0]:
            grid_best = (value, candidate)

    return {
        "kernel": "abs(y1-y2) (Gini U-statistic)",
        "budget": BUDGET,
        "projection_score_s": projection_scores,
        "raw_prediction_mse": raw_mse,
        "optimal_pi_sqrt_s": optimal_pi,
        "raw_residual_pi_sqrt_mse_negative_control": raw_residual_pi,
        "uniform_pi": uniform_pi,
        "leading_objective_optimal": leading_objective(optimal_pi),
        "leading_objective_raw_residual_control": leading_objective(raw_residual_pi),
        "leading_objective_uniform": leading_objective(uniform_pi),
        "finite_grid_best": {"objective": grid_best[0], "pi": grid_best[1], "step": 0.01},
        "clipping_active": any(value >= 1 for value in optimal_pi),
    }


def main() -> None:
    result = calculate()
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
