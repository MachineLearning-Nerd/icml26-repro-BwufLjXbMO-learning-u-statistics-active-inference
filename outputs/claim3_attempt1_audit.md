# Claim 3 — Attempt 1: CRN coupling / CLT audit

## Live claim

> A central limit theorem is established for the normalized AIPW U-statistic under data-adaptive sampling, enabling computable asymptotic confidence intervals via a common-random-number coupling argument (Theorem 2.4).

## Source pin and scope

The retained arXiv source states the active-U CLT at `ICML_Camera-ready.tex` lines 399–427: under the Appendix sampling-policy assumption, `sqrt(n)(U_AIPW^hat-pi - theta*)` converges to a normal law and its plug-in variance produces an asymptotically valid confidence interval. Lines 429 and 889–907 identify the CRN mechanism and state the key HT-functional coupling result.

The assumptions are material: H1 requires uniform positive inclusion probabilities (lines 851–853) and H2 requires `sup_i |hat-pi(X_i)-pi*(X_i)| = O_p(n^-1/2)` (line 854). This attempt does **not** prove the paper's complete U-statistic CLT or coverage result. It directly audits the stated CRN coupling mechanism in a bounded two-stratum HT functional.

## CPU experiment

`src/claim3_crn_coupling.py` uses the same uniforms for oracle and learned Bernoulli decisions, exactly as the source CRN construction specifies. The oracle inclusion range is `[0.35, 0.65]`, satisfying positivity. For `n = 200, 800, 3200`, the learned policy differs by `0.10/sqrt(n)`, satisfying the H2 rate. Across 2,500 seeded replicates per size, RMS values of `sqrt(n)(T_n(hat-pi)-T_n(pi*))` were respectively `0.25454`, `0.17606`, and `0.12384`; they decrease as the H2 error shrinks.

## Negative control

A fixed `0.10` learned-policy error violates H2 while keeping probabilities positive. Its corresponding RMS values remain about `0.95` at all three sizes (`0.95448`, `0.93341`, `0.94846`), so the scaled coupling difference does not become small. The same-uniform coupling is retained in both arms; the changed condition is only the source H2 rate.

## Verdict

**Verified, scoped.** The finite CPU simulation and negative control support the CRN/H1/H2 coupling route that the source uses for Theorem 2.4. It is not a general proof of the normalized AIPW U-statistic CLT, its variance estimator, or confidence-interval coverage.

## Artifacts

- `src/claim3_crn_coupling.py`
- `tests/test_claim3_crn_coupling.py`
- `outputs/claim3_attempt1/result.json`
- `outputs/claim3_attempt1/test.log`
- `outputs/claim3_attempt1/SHA256SUMS`
