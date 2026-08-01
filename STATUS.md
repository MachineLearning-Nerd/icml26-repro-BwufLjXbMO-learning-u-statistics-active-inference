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
- Current phase: claim_5_attempt_2_inconclusive
- Claim 1: verified as a finite scoped AIPW algebra audit; exact enumeration gives absolute error 1.11e-16 and the omitted-IPW control is biased.
- Claim 2: verified as a scoped finite Hoeffding-projection sampling audit; `sqrt(s)` has objective 0.6288614429 versus 0.6565200975 for the raw-residual control. This is not a general asymptotic proof or clipping-boundary test.
- Claim 3: verified as a scoped finite CRN-coupling audit. With H2-sized policy error, scaled RMS differences decrease from 0.25454 to 0.12384; fixed-error H2 control stays near 0.95. This is not a general CLT/coverage proof.
- Claim 4: falsified for literal comparator attribution. The source assigns roughly 60% saving to the distinct classical IPW estimator, while the live claim assigns it to uniform AIPW; this is not represented as an ACS numerical rerun. See `outputs/claim4_falsification_audit.md`.
- Claim 5: Attempt 2 remains inconclusive. Official/history and author-release searches found no source-faithful snapshot/cohort extraction, code/supplement, preprocessing, XGBoost configuration, active-sampling seeds, or 3,000-trial outputs; no proxy clinical evaluation was run.
- Claim 6: unverified
- Next action: Claim 5 Attempt 3 — search archived author/repository release history and paper-source assets for exact protocol artifacts.
- Publication status: not started
