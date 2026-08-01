# Claim 3 — CRN coupling


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_27c3d6930505", "created_at": "2026-08-01T05:59:23+00:00", "title": "Claim 3 — CRN coupling"}
-->
# Claim 3 — CRN coupling for adaptive sampling

**Live claim.** A CLT for the normalized AIPW U-statistic follows through a common-random-number coupling argument.

**Verdict: verified, scoped mechanism audit.** Under source-like H1 positivity and H2 policy error `0.10/sqrt(n)`, 2,500 seeded CPU replicates give scaled RMS coupling differences `0.25454`, `0.17606`, and `0.12384` for `n=200,800,3200`. A fixed-error H2 violation retains RMS near `0.95`.

This supports the finite CRN/H1/H2 mechanism only; it is not a proof of the full U-statistic CLT, variance estimator, or CI coverage.

**Evidence:** `outputs/claim3_attempt1_audit.md`, `outputs/claim3_attempt1/result.json`, `outputs/claim3_attempt1/SHA256SUMS`. Run `.venv/bin/python src/claim3_crn_coupling.py`.

**Links:** [public code](https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference) · [paper](https://arxiv.org/abs/2605.11638). No Jobs or Buckets were used.
