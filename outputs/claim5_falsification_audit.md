# Claim 5 — literal source/protocol falsification attempt

## Exact live claim

> On the VitalDB perioperative dataset, the active Wilcoxon signed-rank test for hemoglobin shifts requires approximately 20% less labeling budget than the classical baseline for equivalent precision (Section 4.2, Figure 2).

## Method

After three source/data/provenance attempts, this final allowed attempt tested only whether the exact live wording contradicts the accepted source. It did not use missing-data availability as a falsification and did not run a proxy clinical experiment.

## Primary-source result

The accepted paper's VitalDB section explicitly describes the hemoglobin paired-difference protocol and Wilcoxon target, then states: “comparable precision with about 20% fewer labels than {classical} baseline,” while maintaining near-nominal coverage. The source does not substitute the uniform baseline for this statement.

## Verdict

**Inconclusive.** No literal source/protocol contradiction was found. The primary source supports the wording, but the unreleased paper-era snapshot, cohort extraction, preprocessing, XGBoost settings, seeds, and trial outputs still prevent an independent source-faithful numerical verification.

Machine-readable result: `outputs/claim5_falsification_result.json`.
