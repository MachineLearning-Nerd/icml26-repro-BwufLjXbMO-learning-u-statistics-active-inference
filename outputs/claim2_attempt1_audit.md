# Claim 2 — Attempt 1: finite optimal-sampling audit

## Live claim

> The variance-minimizing (optimal) sampling probability is proportional to the square root of a residual-uncertainty term derived from the Hoeffding projection, depending on `h1(Y) − h1^mu(Yhat)` rather than the raw prediction error `|Y − Yhat|` (Theorem 2.2, Section 2.2).

## Source pin and derivation target

The pinned source, `upstream/arxiv_source/ICML_Camera-ready.tex`, derives the AIPW Hoeffding decomposition at lines 252–278 and defines the sampling-dependent variance term at lines 274–277. Theorem 2.2 at lines 280–301 defines

` s(X) = E[(h1(Y) - h1^mu(Yhat))^2 | X] `

and gives `pi*(X) ∝ sqrt(s(X))` under the budget constraint (with clipping at one). It explicitly distinguishes this score from the raw prediction residual at lines 301–302.

## Independent finite CPU check

`src/claim2_optimal_sampling.py` implements a three-stratum finite distribution with Gini kernel `h(y1,y2)=|y1-y2|`. It computes the first-order projections directly from the finite joint distribution, calculates the exact conditional projection-residual scores, then minimizes the leading sampling-dependent objective

`sum_x p(x) s(x) / pi(x)`

at expected budget 1.5 labels across the three equally weighted strata. All probabilities are interior, so clipping is inactive.

| Rule | Sampling-dependent objective |
|---|---:|
| `sqrt(s)` (source rule) | 0.6288614429 |
| `sqrt(E[(Y-Yhat)^2|X])` raw-residual control | 0.6565200975 |
| Uniform | 0.6902222222 |

The independent brute-force 0.01-grid search found `[0.72, 0.40, 0.38]` with objective `0.6288823912`, agreeing with the analytic allocation `[0.7207339, 0.3965485, 0.3827177]` to grid precision.

## Negative control

The raw-prediction-residual rule is intentionally the mean-estimation-style comparator that the source says is not generally optimal for U-statistics. It has strictly higher objective than the projection-residual rule (`0.6565200975 > 0.6288614429`). The result therefore distinguishes the theorem's Hoeffding-projection score from an untested restatement of raw prediction error.

## Verdict

**Verified (scoped).** The source states the claimed score and a clean-room finite Gini U-statistic calculation verifies the constrained `sqrt(s)` optimum and rejects the raw-residual alternative. This is not a general asymptotic proof of Theorem 2.2 and does not test the clipping-active boundary.

## Reproduce

```bash
.venv/bin/python src/claim2_optimal_sampling.py > outputs/claim2_attempt1_result.json
.venv/bin/python -m pytest -q
sha256sum -c outputs/claim2_attempt1/SHA256SUMS
```
