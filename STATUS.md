# Status

- OpenReview ID: `BwufLjXbMO`
- Submission number: 10819
- Live claim count / maximum points: 6 / 12
- Selection timestamp: 2026-08-01T04:30:37Z
- Paper: https://arxiv.org/abs/2605.11638
- Source pin: arXiv source archive, SHA-256 in `evidence/SHA256SUMS`
- Official code: no author executable repository identified in the retained arXiv source; clean-room audit required
- Compute policy: Hugging Face `cpu-upgrade` only; no GPU or paid Jobs
- GitHub repository: https://github.com/MachineLearning-Nerd/icml26-repro-BwufLjXbMO-learning-u-statistics-active-inference
- Current phase: claim_4_attempt_1_inconclusive_source_artifact_scope
- Claim 1: verified as a finite scoped AIPW algebra audit; exact enumeration gives absolute error 1.11e-16 and the omitted-IPW control is biased.
- Claim 2: verified as a scoped finite Hoeffding-projection sampling audit; `sqrt(s)` has objective 0.6288614429 versus 0.6565200975 for the raw-residual control. This is not a general asymptotic proof or clipping-boundary test.
- Claim 3: verified as a scoped finite CRN-coupling audit. With H2-sized policy error, scaled RMS differences decrease from 0.25454 to 0.12384; fixed-error H2 control stays near 0.95. This is not a general CLT/coverage proof.
- Claim 4: inconclusive source-artifact audit; source specifies ACS/Gini/XGBoost/budgets/trials but releases no code, ACS version/split, seeds, or trial outputs. No proxy execution was represented as a reproduction.
- Claim 5–6: unverified
- Next action: Claim 4 Attempt 2 — search authoritative author/supplement/ACS provenance for an exact released protocol before considering a source-faithful CPU run.
- Publication status: not started
