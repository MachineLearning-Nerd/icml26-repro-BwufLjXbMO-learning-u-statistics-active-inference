# Learning U-Statistics with Active Inference — ICML 2026 reproduction

OpenReview ID: `BwufLjXbMO`  
Paper: https://arxiv.org/abs/2605.11638

This repository is a CPU-only, evidence-driven reproduction of the live ICML challenge contract. The six live claims are saved verbatim in `contract/live_claims.json`.

## Current status

All six live claims now have durable outcomes: Claims 1–3 are scoped finite mechanism verifications, Claim 4 is a literal comparator-attribution falsification, and Claims 5–6 are inconclusive because the source-faithful empirical artifacts were not released. The local Trackio logbook, poster gates, tests, and official validator are ready for independent review; publication has not started.

## Reproduce setup

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

The paper's arXiv source is retained with a SHA-256 manifest under `evidence/`. No author executable repository was identified in the paper's arXiv source; clean-room implementations will be explicitly labeled.
