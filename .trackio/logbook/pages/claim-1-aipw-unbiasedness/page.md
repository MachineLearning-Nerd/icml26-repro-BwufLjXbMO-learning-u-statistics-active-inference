# Claim 1 — AIPW unbiasedness


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_2fe3e8e4455b", "created_at": "2026-08-01T05:59:21+00:00", "title": "Claim 1 — AIPW unbiasedness"}
-->
# Claim 1 — AIPW unbiasedness

**Live claim.** The AIPW U-statistic estimator is unbiased (Proposition 2.1).

**Verdict: verified, finite scoped audit.** Exact enumeration of 64 joint outcome/sampling cells for a non-uniform positive sampling design gives AIPW error `1.11e-16` at target `0.42`; omitting IPW gives bias `0.0026`.

This verifies the estimator mechanism for a binary pairwise U-statistic under independent sampling, not the full arbitrary-order/adaptive theorem.

**Evidence and reproduction:** `outputs/claim1_attempt1_audit.md`, `outputs/claim1_attempt1/result.json`, `outputs/claim1_attempt1/SHA256SUMS`; run `.venv/bin/python src/claim1_aipw_enumeration.py` then `.venv/bin/python -m pytest -q`.

**Links:** [public code](https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference) · [paper](https://arxiv.org/abs/2605.11638). No Jobs or Buckets were used.
