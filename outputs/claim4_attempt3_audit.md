# Claim 4 — primary ACS archive / protocol audit (Attempt 3)

**Exact live claim:** On the ACS income dataset, active sampling for the Gini index achieves roughly 60% labeling-budget reduction relative to **uniform** sampling while maintaining 90% confidence-interval coverage.

## Independent primary-provenance route

This attempt did not repeat author-repository or supplement searches. It fetched and retained Census primary records:

- [ACS microdata](https://www.census.gov/programs-surveys/acs/microdata.html)
- [2023 ACS PUMS 1-Year archive](https://www2.census.gov/programs-surveys/acs/data/pums/2023/1-Year/)
- [2022 ACS PUMS 1-Year archive](https://www2.census.gov/programs-surveys/acs/data/pums/2022/1-Year/)

Both archive directories returned HTTP 200 and have distinct SHA-256 listing hashes. Thus a source-faithful ACS run requires the paper to specify a particular Census release/product and extraction.

## Source comparison

The paper identifies ACS income data and XGBoost prediction/proxy models, but its ACS section does not specify the ACS/PUMS release year/product, geography/eligibility filters, income transformation/features, split/seeds, XGBoost/proxy configuration, or replicate outputs. The source explicitly says the approximately 60% budget reduction is relative to **classical**, while it does not state that same reduction relative to **uniform**.

## Result

No exact source-faithful CPU experiment was run: selecting any currently available ACS archive would be a proxy. This attempt is **inconclusive**, not verification or falsification. The exact source-comparator discrepancy and the missing primary protocol leave one permitted next step: a literal comparator-scope falsification audit.

## Retained evidence

- `evidence/claim4_attempt3/retrieval.tsv`
- `evidence/claim4_attempt3/response_1.html` through `response_6.html`
- `evidence/claim4_attempt3/SHA256SUMS`
- `outputs/claim4_attempt3_result.json`
- `outputs/claim4_attempt3_test.log` (13 passed)
