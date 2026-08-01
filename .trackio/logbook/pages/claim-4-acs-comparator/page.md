# Claim 4 — ACS comparator


---
<!-- trackio-cell
{"type": "markdown", "id": "cell_5894d0c806dd", "created_at": "2026-08-01T05:59:24+00:00", "title": "Claim 4 — ACS comparator"}
-->
# Claim 4 — ACS Gini labeling reduction

**Live claim.** ACS active sampling achieves roughly 60% labeling-budget reduction relative to uniform sampling while maintaining 90% coverage.

**Verdict: falsified for literal comparator attribution.** The pinned paper assigns the roughly 60% reduction to the distinct **classical IPW** estimator. It separately defines uniform as AIPW under uniform sampling; it does not report the same figure relative to uniform AIPW.

This is a wording/comparator falsification, not an ACS numerical rerun. The source-faithful ACS code, data split, seeds, and outputs were not released.

**Evidence:** `outputs/claim4_falsification_audit.md`, `outputs/claim4_falsification_result.json`, `outputs/claim4_falsification_SHA256SUMS`; run `.venv/bin/python src/claim4_falsification_comparator_audit.py`.

**Links:** [public code](https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference) · [paper](https://arxiv.org/abs/2605.11638). No Jobs or Buckets were used.
