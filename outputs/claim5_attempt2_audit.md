# Claim 5 — Attempt 2: official/history and author-release provenance audit

## Exact live claim

> On the VitalDB perioperative dataset, the active Wilcoxon signed-rank test for hemoglobin shifts requires approximately 20% less labeling budget than the classical baseline for equivalent precision (Section 4.2, Figure 2).

## Distinct route

This attempt did not repeat the Attempt-1 API-access audit. It searched retained official ICML virtual-paper material, exact-title and author-name GitHub repository results, authenticated GitHub code-search results, and the current official VitalDB pages/API for a paper-era release or reproducible protocol.

## Evidence

- The pinned source retains the high-level cohort/window/outcome/XGBoost/3,000-trial/comparator description.
- Exact-title and author-query GitHub repository searches returned zero repositories. The code search returned this reproduction repository and an automated paper-index entry, but no author executable.
- The ICML virtual page contains the abstract, but no release/supplement/code marker.
- Current VitalDB pages and cases API are reachable, but they do not identify an accepted snapshot, case extraction, cohort IDs, or paper-era experiment manifest.
- The source still omits the selected records, covariate preprocessing, XGBoost settings, pilot/fold construction, active-sampling seeds, and 3,000 trial outputs.

Responses, statuses, and hashes are retained in `evidence/claim5_attempt2/`; the machine-readable audit is `outputs/claim5_attempt2_result.json`.

## Decision

No source-faithful CPU rerun is possible from the recovered materials. No proxy clinical evaluation was run.

**Verdict: inconclusive (author-release/history availability audit).**

## Next action

Attempt 3: inspect archived author/repository release history and paper-source assets. If the exact protocol remains unavailable, proceed to the single allowed falsification attempt without asserting a proxy result.
