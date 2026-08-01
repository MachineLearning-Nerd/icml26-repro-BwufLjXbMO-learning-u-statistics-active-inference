# Claim 4 — ACS source/protocol availability audit (Attempt 1)

**Exact live claim:** On the ACS income dataset, active sampling for the Gini
index achieves roughly 60% labeling-budget reduction relative to uniform
sampling while maintaining 90% confidence-interval coverage.

## What the pinned primary source supports

The arXiv source (`ICML_Camera-ready.tex`) states ACS income/Gini use,
XGBoost-based prediction and score models, budgets 800/4800/8800/12000/16000,
90% intervals, 3,000 trials, and a qualitative “roughly 60%” saving relative
to classical sampling. It does **not** make the live wording's comparison to
uniform sampling at that value explicit: Figure 1 describes active as larger
than both baselines, while Section 4.1 names the 60% comparison as classical.

## Availability decision

The retained release contains TeX, style files, and rendered figures only. It
contains no experiment code, ACS/Folktables snapshot/version, preprocessing,
split, XGBoost hyperparameters/seeds, sampling runner, or trial outputs.
Consequently no source-faithful CPU experiment was run. A newly downloaded ACS
run would be a proxy and is not represented as a full reproduction.

**Outcome:** `inconclusive_source_artifact_scope`.

## Evidence

- Structured audit: `outputs/claim4_attempt1_result.json`
- Source pin/hash: `evidence/SHA256SUMS`
- Command: `.venv/bin/python src/claim4_acs_availability_audit.py`
- Tests: `.venv/bin/python -m pytest -q` (see `outputs/claim4_attempt1_test.log`)
