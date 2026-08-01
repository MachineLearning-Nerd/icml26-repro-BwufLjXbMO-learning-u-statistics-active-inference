# Claim 1 — Attempt 1: finite AIPW enumeration

## Live claim

> The AIPW U-statistic estimator using augmented inverse probability weighting is proven unbiased, satisfying \(E[U_{AIPW}^\pi]=\theta^*\) (Proposition 2.1).

## Source mapping

The pinned source defines the estimator in `upstream/arxiv_source/ICML_Camera-ready.tex`, lines 233–238, and states Proposition 2.1 at lines 242–245.  For each tuple the correction is multiplied by the product of inclusion indicators divided by the product of their sampling probabilities.

## Method

`src/claim1_aipw_enumeration.py` exactly enumerates:

- three iid binary outcomes with \(P(Y=1)=0.3\);
- all eight outcome assignments and all eight independent sampling assignments (64 joint cells);
- pairwise kernel \(h(y_i,y_j)=|y_i-y_j|\);
- non-uniform positive probabilities \((0.20,0.55,0.80)\); and
- deterministic prediction values \((0.10,0.70,0.40)\).

The exact target is \(\theta^*=2p(1-p)=0.42\). Conditionally on any outcome assignment, the inclusion product has expectation equal to the inclusion-probability product, so the IPW correction has expectation equal to the original residual U-statistic term.

## Result

| Quantity | Exact-enumeration result |
|---|---:|
| \(\theta^*\) | 0.42 |
| \(E[U(Y)]\) | 0.4199999999999999 |
| \(E[U^\pi_{AIPW}]\) | 0.4199999999999999 |
| absolute AIPW error | \(1.11\times10^{-16}\) |
| maximum conditional error versus \(U(Y)\) | 0.0 |

## Negative control

The control omits inverse-probability weighting while retaining the same plug-in and residual terms. Its expectation is 0.4174, with absolute bias 0.0026, confirming that the observed equality is not due to the plug-in term alone under non-uniform sampling.

## Verdict and scope

**Verified (finite scoped audit).** This exactly checks the algebraic unbiasedness mechanism of the stated AIPW estimator under independent positive sampling for a nontrivial pairwise U-statistic. It is not a general proof of Proposition 2.1 for arbitrary kernel order, outcome distribution, or adaptive sampling.

## Reproduction

```bash
.venv/bin/python src/claim1_aipw_enumeration.py
.venv/bin/python -m pytest -q
sha256sum -c outputs/claim1_attempt1/SHA256SUMS
```

Retained outputs: `outputs/claim1_attempt1/result.json`, `run.log`, `test.log`, and `SHA256SUMS`.
