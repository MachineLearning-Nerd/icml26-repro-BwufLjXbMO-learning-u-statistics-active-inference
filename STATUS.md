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
- Current phase: claim_2_attempt_1_scoped_verified
- Claim 1: verified as a finite scoped AIPW algebra audit; exact enumeration gives absolute error 1.11e-16 and the omitted-IPW control is biased.
- Claim 2: verified as a scoped finite Hoeffding-projection sampling audit; `sqrt(s)` has objective 0.6288614429 versus 0.6565200975 for the raw-residual control. This is not a general asymptotic proof or clipping-boundary test.
- Claim 3–6: unverified
- Publication status: not started
