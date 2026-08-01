# Executive summary

**Scope.** CPU-only clean-room audit of the six live claims for *Learning U-Statistics with Active Inference* (OpenReview `BwufLjXbMO`). The official source archive is pinned in `evidence/SHA256SUMS`; no author executable repository was identified.

| Outcome | Claims | Interpretation |
|---|---|---|
| Scoped verification | 1–3 | Finite CPU checks verify the claimed algebra, sampling-allocation, and CRN-coupling mechanisms, not their full asymptotic theorems. |
| Literal-source falsification | 4 | The reported ~60% ACS reduction is against the classical estimator, not the live claim's uniform AIPW comparator. |
| Inconclusive | 5–6 | The source supports the wording, but no paper-era data/configuration/trial outputs enable a source-faithful numerical rerun. |

| Resource | Value |
|---|---|
| Compute | Local CPU only; no HF Jobs, GPU, or paid compute used |
| Public implementation | https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference |
| Paper | https://arxiv.org/abs/2605.11638 |
| Source archive | `evidence/arxiv_source.tar`, SHA-256 manifest `evidence/SHA256SUMS` |
| Reproduction command | `.venv/bin/python -m pytest -q` |

The poster is embedded below from `logbook/poster_embed.html`.
