# Claim 5 — Attempt 1: VitalDB source/protocol availability audit

## Exact live claim

> On the VitalDB perioperative dataset, the active Wilcoxon signed-rank test for hemoglobin shifts requires approximately 20% less labeling budget than the classical baseline for equivalent precision (Section 4.2, Figure 2).

## Pinned source facts

The retained arXiv source (`upstream/arxiv_source/ICML_Camera-ready.tex`) describes 6,388 surgical cases; anesthesia start as the index event; the most recent pre-event and earliest post-event hemoglobin measurements inside a ±24-hour window; `D = Yᵃ − Yᵇ`; XGBoost for both prediction and score models; 760 perioperative labels in a two-fold scheme; and 3,000 labeling-decision trials. It says comparable precision uses about 20% fewer labels than the **classical** baseline and 10% fewer than uniform sampling.

The source bundle supplies Figure 2 (`Figure/combined_wilcoxon.pdf`), but does not supply the numerical figure series, selected-case cohort, experiment code, trial outputs, or a reproducible dataset manifest.

## Primary external data evidence

Retrieved endpoints and SHA-256 hashes are retained in `evidence/claim5_attempt1/`:

- [VitalDB dataset/data-use page](https://vitaldb.net/dataset/) — HTTP 200; the retrieved agreement states CC BY-NC-SA 4.0 subject to its terms.
- [VitalDB cases API](https://api.vitaldb.net/cases) — HTTP 200.
- [VitalDB labs API](https://api.vitaldb.net/labs) — HTTP 200.
- [VitalDB tracks API](https://api.vitaldb.net/trks) — HTTP 200.
- [VitalDB utilities repository](https://github.com/vitaldb/vitalutils) — HTTP 200.

Those public endpoints establish that VitalDB documentation/API material is reachable; they do **not** identify the paper's accepted dataset snapshot, selected cohort, case-level extraction, preprocessing, or experiment configuration.

## Decision

No source-faithful CPU run was performed. A proxy cohort, newly chosen XGBoost configuration, or arbitrary active-sampling seeds would not reproduce the claimed Figure-2 comparison.

**Verdict: inconclusive (availability/protocol audit).** This attempt neither verifies nor falsifies the approximately-20% result.

## Next action

Attempt 2 must search official VitalDB version/history and author supplementary/code releases for the missing accepted snapshot, cohort extraction, preprocessing, XGBoost configuration, labeling budgets/seeds, and 3,000-trial outputs.
