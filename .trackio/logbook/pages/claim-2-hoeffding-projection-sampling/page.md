# Claim 2 — Hoeffding-projection sampling


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_9ba3a26e2cf0", "created_at": "2026-08-01T05:59:22+00:00", "title": "Claim 2 — Hoeffding-projection sampling"}
-->
# Claim 2 — Hoeffding-projection sampling score

**Live claim.** The variance-minimizing sampling probability is proportional to the square root of a Hoeffding projection-residual uncertainty score, not raw prediction error.

**Verdict: verified, scoped finite audit.** A clean-room three-stratum Gini U-statistic calculation gives objective `0.6288614429` for the source `sqrt(s)` allocation, versus `0.6565200975` for the raw-residual control and `0.6902222222` for uniform allocation. A brute-force grid agrees with the analytic allocation.

This is an interior, finite calculation; it does not prove the full asymptotic theorem or clipping-active boundary.

**Evidence:** `outputs/claim2_attempt1_audit.md`, `outputs/claim2_attempt1/result.json`, `outputs/claim2_attempt1/SHA256SUMS`. Run `.venv/bin/python src/claim2_optimal_sampling.py` and `.venv/bin/python -m pytest -q`.

**Links:** [public code](https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference) · [paper](https://arxiv.org/abs/2605.11638). No Jobs or Buckets were used.
