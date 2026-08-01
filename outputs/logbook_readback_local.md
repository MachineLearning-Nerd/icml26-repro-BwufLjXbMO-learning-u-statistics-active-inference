# Learning U-Statistics with Active Inference

## Pages

| Page |
| --- |
| [Executive summary](#/executive-summary) |
| [Claim 1 — AIPW unbiasedness](#/claim-1-aipw-unbiasedness) |
| [Claim 2 — Hoeffding-projection sampling](#/claim-2-hoeffding-projection-sampling) |
| [Claim 3 — CRN coupling](#/claim-3-crn-coupling) |
| [Claim 4 — ACS comparator](#/claim-4-acs-comparator) |
| [Claim 5 — VitalDB](#/claim-5-vitaldb) |
| [Claim 6 — Political bias](#/claim-6-political-bias) |
| [Conclusion](#/conclusion) |

> Agent view: markdown bodies are inline; code cells show the command, a code head, and an output tail; figures inline small raw data. Fetch full payloads with `trackio logbook read cell <id> [--full|--raw|--html]`.

## Executive summary · `executive-summary`

### Executive summary · markdown · `cell_61a9e80a39d6` · 2026-08-01 05:59

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

### Reproduction poster · markdown · `cell_4de0de19eef5` · 2026-08-01 05:59

<iframe title="Reproduction poster" src="poster.html" style="width:100%;height:680px;border:0;border-radius:12px"></iframe>

### Reproduction poster · figure · `cell_1f7aa9e2dcbd` · 2026-08-01 06:07

HTML figure: 416.3k chars (--html).

## Claim 1 — AIPW unbiasedness · `claim-1-aipw-unbiasedness`

### Claim 1 — AIPW unbiasedness · markdown · `cell_2fe3e8e4455b` · 2026-08-01 05:59

**Live claim.** The AIPW U-statistic estimator is unbiased (Proposition 2.1).

**Verdict: verified, finite scoped audit.** Exact enumeration of 64 joint outcome/sampling cells for a non-uniform positive sampling design gives AIPW error `1.11e-16` at target `0.42`; omitting IPW gives bias `0.0026`.

This verifies the estimator mechanism for a binary pairwise U-statistic under independent sampling, not the full arbitrary-order/adaptive theorem.

**Evidence and reproduction:** `outputs/claim1_attempt1_audit.md`, `outputs/claim1_attempt1/result.json`, `outputs/claim1_attempt1/SHA256SUMS`; run `.venv/bin/python src/claim1_aipw_enumeration.py` then `.venv/bin/python -m pytest -q`.

**Links:** [public code](https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference) · [paper](https://arxiv.org/abs/2605.11638). No Jobs or Buckets were used.

## Claim 2 — Hoeffding-projection sampling · `claim-2-hoeffding-projection-sampling`

### Claim 2 — Hoeffding-projection sampling · markdown · `cell_9ba3a26e2cf0` · 2026-08-01 05:59

# Claim 2 — Hoeffding-projection sampling score

**Live claim.** The variance-minimizing sampling probability is proportional to the square root of a Hoeffding projection-residual uncertainty score, not raw prediction error.

**Verdict: verified, scoped finite audit.** A clean-room three-stratum Gini U-statistic calculation gives objective `0.6288614429` for the source `sqrt(s)` allocation, versus `0.6565200975` for the raw-residual control and `0.6902222222` for uniform allocation. A brute-force grid agrees with the analytic allocation.

This is an interior, finite calculation; it does not prove the full asymptotic theorem or clipping-active boundary.

**Evidence:** `outputs/claim2_attempt1_audit.md`, `outputs/claim2_attempt1/result.json`, `outputs/claim2_attempt1/SHA256SUMS`. Run `.venv/bin/python src/claim2_optimal_sampling.py` and `.venv/bin/python -m pytest -q`.

**Links:** [public code](https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference) · [paper](https://arxiv.org/abs/2605.11638). No Jobs or Buckets were used.

## Claim 3 — CRN coupling · `claim-3-crn-coupling`

### Claim 3 — CRN coupling · markdown · `cell_27c3d6930505` · 2026-08-01 05:59

# Claim 3 — CRN coupling for adaptive sampling

**Live claim.** A CLT for the normalized AIPW U-statistic follows through a common-random-number coupling argument.

**Verdict: verified, scoped mechanism audit.** Under source-like H1 positivity and H2 policy error `0.10/sqrt(n)`, 2,500 seeded CPU replicates give scaled RMS coupling differences `0.25454`, `0.17606`, and `0.12384` for `n=200,800,3200`. A fixed-error H2 violation retains RMS near `0.95`.

This supports the finite CRN/H1/H2 mechanism only; it is not a proof of the full U-statistic CLT, variance estimator, or CI coverage.

**Evidence:** `outputs/claim3_attempt1_audit.md`, `outputs/claim3_attempt1/result.json`, `outputs/claim3_attempt1/SHA256SUMS`. Run `.venv/bin/python src/claim3_crn_coupling.py`.

**Links:** [public code](https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference) · [paper](https://arxiv.org/abs/2605.11638). No Jobs or Buckets were used.

## Claim 4 — ACS comparator · `claim-4-acs-comparator`

### Claim 4 — ACS comparator · markdown · `cell_5894d0c806dd` · 2026-08-01 05:59

# Claim 4 — ACS Gini labeling reduction

**Live claim.** ACS active sampling achieves roughly 60% labeling-budget reduction relative to uniform sampling while maintaining 90% coverage.

**Verdict: falsified for literal comparator attribution.** The pinned paper assigns the roughly 60% reduction to the distinct **classical IPW** estimator. It separately defines uniform as AIPW under uniform sampling; it does not report the same figure relative to uniform AIPW.

This is a wording/comparator falsification, not an ACS numerical rerun. The source-faithful ACS code, data split, seeds, and outputs were not released.

**Evidence:** `outputs/claim4_falsification_audit.md`, `outputs/claim4_falsification_result.json`, `outputs/claim4_falsification_SHA256SUMS`; run `.venv/bin/python src/claim4_falsification_comparator_audit.py`.

**Links:** [public code](https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference) · [paper](https://arxiv.org/abs/2605.11638). No Jobs or Buckets were used.

## Claim 5 — VitalDB · `claim-5-vitaldb`

### Claim 5 — VitalDB · markdown · `cell_12444d6596e0` · 2026-08-01 05:59

# Claim 5 — VitalDB Wilcoxon labeling reduction

**Live claim.** Active Wilcoxon signed-rank testing on VitalDB needs about 20% less labeling than the classical baseline for equivalent precision.

**Verdict: inconclusive.** The accepted source explicitly supports the 20%-versus-classical wording. Three independent availability/provenance attempts plus a literal-source falsification attempt found no contradiction, but no paper-era data snapshot, cohort/case manifest, preprocessing, XGBoost configuration, seed, or 3,000-trial output was released for a numerical rerun.

No proxy clinical experiment was run and missing artifacts were not called a falsification.

**Evidence:** `outputs/claim5_attempt1_audit.md`, `outputs/claim5_attempt2_audit.md`, `outputs/claim5_attempt3_audit.md`, `outputs/claim5_falsification_audit.md`; manifests are stored beside retained outputs/evidence.

**Links:** [public code](https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference) · [paper](https://arxiv.org/abs/2605.11638) · [VitalDB](https://vitaldb.net/). No Jobs or Buckets were used.

## Claim 6 — Political bias · `claim-6-political-bias`

### Claim 6 — Political bias · markdown · `cell_5956d03b0796` · 2026-08-01 05:59

# Claim 6 — Political-bias Kendall tau labeling reduction

**Live claim.** Active Kendall-tau estimation for political-bias LLM labels saves about 20% versus classical and 10% versus uniform sampling.

**Verdict: inconclusive.** The pinned source matches the live political-bias/Kendall target and both comparator-specific savings. Three independent release/archive/provenance attempts plus a literal-source falsification attempt found no wording contradiction. However, selected-paper data, GPT-3.5/GPT-4 outputs, configuration, seeds, and 3,000-trial artifacts are unavailable.

No related prior-work repository was used as a source-faithful proxy.

**Evidence:** `outputs/claim6_attempt1_audit.md`, `outputs/claim6_attempt2_audit.md`, `outputs/claim6_attempt3_audit.md`, `outputs/claim6_falsification_result.json`.

**Links:** [public code](https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference) · [paper](https://arxiv.org/abs/2605.11638). No Jobs or Buckets were used.

## Conclusion · `conclusion`

### Conclusion · markdown · `cell_be793becb39e` · 2026-08-01 05:59

This CPU-only reproduction produced three scoped mechanism verifications (Claims 1–3), one literal comparator-attribution falsification (Claim 4), and two inconclusive empirical claims (Claims 5–6). The inconclusive claims are not negative evidence: source wording was supported, but source-faithful numerical inputs and outputs were not released.

All source hashes, scripts, tests, command logs, and evidence paths are in the public repository. The work used no Hugging Face Jobs, Buckets, GPUs, or paid compute. Reproduction is intentionally limited to the scope documented on each claim page.

