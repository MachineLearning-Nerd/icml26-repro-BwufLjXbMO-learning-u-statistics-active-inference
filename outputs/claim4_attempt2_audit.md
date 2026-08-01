# Claim 4 — authoritative-material / ACS-provenance audit (Attempt 2)

**Exact live claim:** On the ACS income dataset, active sampling for the Gini
index achieves roughly 60% labeling-budget reduction relative to **uniform**
sampling while maintaining 90% confidence-interval coverage.

## Sources searched

The retained evidence records HTTPS retrieval of the public arXiv v1 record,
OpenReview forum page, OpenReview API endpoint, and two GitHub repository
searches (exact title and `AIPW U-statistic`). The OpenReview API returned 403
without authentication; the public forum/arXiv pages returned 200. Both GitHub
searches returned zero repositories. No direct GitHub link is present in the
retained arXiv or OpenReview page responses.

## Result

No authoritative author executable, supplement, code, ACS snapshot/extraction,
preprocessing/split, XGBoost configuration/seeds, or 3,000-trial outputs were
recovered. Therefore no source-faithful CPU evaluation was run.

The source itself makes a material wording distinction: Figure 1 compares
active, classical, and uniform methods, but the roughly 60% reduction is
explicitly stated **relative to classical**, while all methods are reported as
near-nominal coverage. This does not establish the live claim's 60% comparison
to uniform, and missing artifacts prevent a direct empirical resolution.

**Outcome:** `inconclusive_source_artifact_scope`, not a refutation of the
method and not a proxy reproduction.

## Retained evidence

- `evidence/claim4_attempt2/retrieval.tsv`
- `evidence/claim4_attempt2/response_1` through `response_5`
- `evidence/claim4_attempt2/SHA256SUMS`
- structured result: `outputs/claim4_attempt2_result.json`
