# Claim 6 — Attempt 1: accepted-source political-bias protocol audit

## Live claim

> On the political-bias dataset, active estimation of Kendall's τ for LLM label quality reduces the labeling budget by about 20% versus the classical baseline and about 10% versus uniform sampling (Section 4.3, Figure 3).

## Method and retained source evidence

This CPU-only attempt audits the pinned accepted arXiv source package, not a proxy political-bias experiment. `src/claim6_political_bias_source_audit.py` verifies that the source:

- defines the Kendall τ sign-kernel target for true political labels and GPT-3.5 labels (source lines 775–797);
- reports about 20% fewer labels than the classical baseline and about 10% fewer than uniform (line 796);
- says GPT-4 predictions estimate the uncertainty function and results average 3,000 trials (line 1421); and
- includes `Figure/combined_kendall.pdf`.

The source-specific negative control swaps the comparator labels. It fails: the accepted source does **not** support 20% versus uniform or 10% versus classical. This prevents treating the two baselines as interchangeable.

## Result

**Verdict: inconclusive.** The accepted paper supports the textual comparator-specific result, but its source package contains no political-bias data snapshot, ground-truth labels, GPT-3.5/GPT-4 outputs, estimator implementation, split, seed, budget-to-precision interpolation, or 3,000-trial outputs. The published figure is not enough to regenerate the numerical claim. No proxy LLM/data experiment was run.

## Reproduction

```bash
.venv/bin/python src/claim6_political_bias_source_audit.py
sha256sum -c outputs/claim6_attempt1/SHA256SUMS
.venv/bin/python -m pytest -q
```

Artifacts: `outputs/claim6_attempt1/result.json`, `source_asset_inventory.txt`, and `SHA256SUMS`.
