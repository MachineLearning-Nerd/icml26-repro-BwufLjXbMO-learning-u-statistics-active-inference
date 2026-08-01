# Claim 6 — Attempt 2: authoritative author/release audit

## Live claim

> On the political-bias dataset, active estimation of Kendall's τ for LLM label quality reduces the labeling budget by about 20% versus the classical baseline and about 10% versus uniform sampling (Section 4.3, Figure 3).

## Method

This attempt searched retained authoritative GitHub API results for the selected paper's exact title, the cited prior-work title, and author identities. It then inspected the complete recursive tree and `bias.ipynb` API payload of the only relevant public prior-work repository, `lphLeo/Robust-Active-Statistical-Inference`.

## Result

**Verdict: inconclusive.** Exact-title GitHub search returned zero repositories for the selected paper. The prior-work repository is not a release by the selected paper's authors and cannot reproduce this paper's result: its public `bias.ipynb` requires an untracked `data/bias_dataset.csv` and uses GPT-4o fields, while the selected paper specifies GPT-3.5 predictions and GPT-4 uncertainty. Its tree contains no political-bias snapshot, selected-paper LLM outputs, configuration, seeds, 3,000-trial artifacts, or Figure-3 numerical output.

No proxy experiment was run. The related repository is retained only as provenance showing why it is not a source-faithful substitute.

## Reproduction

```bash
.venv/bin/python src/claim6_attempt2_authoritative_release_audit.py
sha256sum -c outputs/claim6_attempt2/SHA256SUMS
.venv/bin/python -m pytest -q
```
