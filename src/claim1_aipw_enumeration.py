#!/usr/bin/env python3
"""Exact finite audit of Equation (AIPW_pi) / Proposition 2.1.

For a pairwise binary kernel h(y_i,y_j)=|y_i-y_j|, enumerate every outcome
and independent Bernoulli sampling assignment.  The source estimator is

 U_AIPW = U(yhat) + mean_{i<j}[(h(Y_i,Y_j)-h(yhat_i,yhat_j))
                                  xi_i xi_j/(pi_i pi_j)].

Conditionally on outcomes, E_xi[xi_i xi_j/(pi_i pi_j)] = 1 under positivity;
therefore it equals the ordinary U statistic.  The exhaustive calculation
also checks the outer expectation over iid Bernoulli outcomes.  The `bad`
control deliberately omits inverse-probability weights.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "claim1_attempt1"

P_Y = 0.30
PI = (0.20, 0.55, 0.80)  # non-uniform but strictly positive
YHAT = (0.10, 0.70, 0.40)
PAIRS = tuple(itertools.combinations(range(3), 2))


def h(a: float, b: float) -> float:
    return abs(a - b)


def u(values: tuple[float, ...]) -> float:
    return sum(h(values[i], values[j]) for i, j in PAIRS) / len(PAIRS)


def aipw(y: tuple[int, ...], xi: tuple[int, ...]) -> float:
    plug_in = u(YHAT)
    correction = 0.0
    for i, j in PAIRS:
        delta = h(y[i], y[j]) - h(YHAT[i], YHAT[j])
        correction += delta * xi[i] * xi[j] / (PI[i] * PI[j])
    return plug_in + correction / len(PAIRS)


def bad_unweighted(y: tuple[int, ...], xi: tuple[int, ...]) -> float:
    plug_in = u(YHAT)
    correction = 0.0
    for i, j in PAIRS:
        delta = h(y[i], y[j]) - h(YHAT[i], YHAT[j])
        correction += delta * xi[i] * xi[j]
    return plug_in + correction / len(PAIRS)


def outcome_probability(y: tuple[int, ...]) -> float:
    return (P_Y ** sum(y)) * ((1 - P_Y) ** (len(y) - sum(y)))


def sampling_probability(xi: tuple[int, ...]) -> float:
    result = 1.0
    for observed, pi in zip(xi, PI):
        result *= pi if observed else 1 - pi
    return result


def run() -> dict:
    expected_aipw = expected_bad = expected_u = 0.0
    max_conditional_error = 0.0
    conditional_rows = []
    for y in itertools.product((0, 1), repeat=3):
        y = tuple(y)
        conditional_aipw = conditional_bad = 0.0
        for xi in itertools.product((0, 1), repeat=3):
            xi = tuple(xi)
            q = sampling_probability(xi)
            conditional_aipw += q * aipw(y, xi)
            conditional_bad += q * bad_unweighted(y, xi)
        target_u = u(y)
        max_conditional_error = max(max_conditional_error, abs(conditional_aipw - target_u))
        py = outcome_probability(y)
        expected_aipw += py * conditional_aipw
        expected_bad += py * conditional_bad
        expected_u += py * target_u
        conditional_rows.append({
            "y": list(y), "P_y": py, "U_y": target_u,
            "E_xi_AIPW": conditional_aipw,
            "E_xi_bad_unweighted": conditional_bad,
        })
    theta_star = 2 * P_Y * (1 - P_Y)
    return {
        "source": {
            "equation": "ICML_Camera-ready.tex lines 233-245 (Equation AIPW_pi / Proposition 2.1)",
            "kernel": "h(y_i,y_j)=|y_i-y_j|", "n": 3, "r": 2,
            "positivity": list(PI), "iid_bernoulli_outcome_probability": P_Y,
            "predictions": list(YHAT),
        },
        "enumeration_cells": 64,
        "theta_star": theta_star,
        "E_U_y": expected_u,
        "E_AIPW": expected_aipw,
        "AIPW_abs_error_vs_theta_star": abs(expected_aipw - theta_star),
        "max_conditional_AIPW_abs_error_vs_U_y": max_conditional_error,
        "E_bad_unweighted": expected_bad,
        "bad_unweighted_abs_bias_vs_theta_star": abs(expected_bad - theta_star),
        "result": "AIPW matches theta* exactly to floating-point precision; the omitted-IPW control is biased under non-uniform sampling.",
        "conditional_rows": conditional_rows,
    }


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    payload = run()
    (OUT / "result.json").write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps({key: payload[key] for key in (
        "theta_star", "E_AIPW", "AIPW_abs_error_vs_theta_star",
        "E_bad_unweighted", "bad_unweighted_abs_bias_vs_theta_star")}, indent=2))
