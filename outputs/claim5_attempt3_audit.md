# Claim 5 — Attempt 3: accepted-source asset and archival provenance audit

## Exact live claim

> On the VitalDB perioperative dataset, the active Wilcoxon signed-rank test for hemoglobin shifts requires approximately 20% less labeling budget than the classical baseline for equivalent precision (Section 4.2, Figure 2).

## Distinct route

This attempt inspected the accepted arXiv source package and its retained source assets, rather than repeating the previous VitalDB endpoint or author-repository searches. It cross-references the retained official/author archival evidence from Attempts 1–2 without re-querying those endpoints.

## Evidence

The accepted source does state the 6,388-case VitalDB setting, the ±24-hour hemoglobin pairing rule, paired outcome, XGBoost use, 3,000 trial averaging, the approximately 20% classical-baseline statement, and includes `Figure/combined_wilcoxon.pdf`.

Its complete source package contains TeX/styles/bibliography and figure PDFs, but no executable, dataset snapshot, case list, preprocessing manifest, XGBoost configuration, pilot/fold assignment, random seed, model serialization, or trial-output artifact. The retained official VitalDB and author/history records from Attempts 1–2 likewise do not identify those paper-era inputs. Therefore the reported 20% number cannot be independently rerun source-faithfully. No proxy clinical cohort was created or evaluated.

Machine-readable result: `outputs/claim5_attempt3/result.json`; source inventory and hashes: `outputs/claim5_attempt3/`.

## Decision

**Verdict: inconclusive.** This is an authoritative absence/provenance certificate, not a numerical refutation or verification.

## Next action

Run the single permitted Claim 5 falsification attempt against literal source/protocol scope; do not run a proxy VitalDB experiment.
