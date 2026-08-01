# Claim 6 — Attempt 3: archive and dataset-provenance audit

**Outcome:** inconclusive; no proxy political-bias run was performed.

This independent attempt inspected the accepted selected-paper arXiv source inventory, the paper's stated political-bias protocol, authoritative arXiv metadata for the cited related bias-setting work, and a retained GitHub exact-title search response.

## Findings

- The selected source states the political-bias protocol uses GPT-3.5 predictions, GPT-4 uncertainty, and 3,000 trials.
- Its source archive contains no executable, data, configuration, seed, LLM-output, or trial-result asset for that experiment.
- The retained arXiv query establishes the cited `Can Unconfident LLM Annotations Be Used for Confident Conclusions?` record, but that is related-work metadata, not a selected-paper data/release artifact.
- The retained exact-title GitHub repository search returned zero results. Anonymous GitHub code search returned HTTP 401, so it was not treated as evidence of data absence.

`outputs/claim6_attempt3/result.json` and `evidence/claim6_attempt3/` retain the machine-readable facts, raw responses, inventory, and checksums. The next required step is the one literal-source falsification attempt.
