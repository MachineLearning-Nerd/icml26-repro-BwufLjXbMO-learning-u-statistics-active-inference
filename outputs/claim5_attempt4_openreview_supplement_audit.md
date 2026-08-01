# Claim 5 — Attempt 4: official OpenReview supplement-access audit

## Distinct primary-source route

This post-fallback research attempt queried the official OpenReview forum and both public note API routes for `BwufLjXbMO`, rather than repeating VitalDB, author-GitHub, or arXiv-package checks.

## Retained result

- The public forum returned HTTP 200 with a Turnstile verification challenge.
- `api2.openreview.net/notes?forum=BwufLjXbMO` returned HTTP 403.
- `api.openreview.net/notes?forum=BwufLjXbMO` returned HTTP 403.

Evidence, headers, response bodies, endpoint list, and checksums are in `evidence/claim5_attempt4/`; the machine-readable result is `outputs/claim5_attempt4/result.json`.

## Verdict

**Inconclusive.** These access controls do not establish that no supplement exists. They establish only that no public, autonomously retrievable OpenReview attachment/protocol is available through these official routes. The missing VitalDB snapshot, selected-case manifest, preprocessing, XGBoost configuration, seeds, and 3,000-trial outputs therefore remain unresolved.

## Next action

Do not repeat this same access check. Continue Claim 5 only if a new public source-faithful artifact becomes available; otherwise retain the inconclusive evidence and proceed with logbook/review work.
