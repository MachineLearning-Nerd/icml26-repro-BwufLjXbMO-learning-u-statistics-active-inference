# Claim 4 — literal comparator-scope falsification

**Exact live claim:** On the ACS income dataset, active sampling for the Gini index achieves roughly 60% labeling-budget reduction relative to **uniform** sampling while maintaining 90% confidence-interval coverage.

## Question tested

This is a source-attribution falsification only. It tests whether the pinned paper supports the live claim's `60% relative to uniform` comparator. It does **not** treat unavailable ACS code/data as a numerical counterexample and does not claim an ACS rerun.

## Primary-source check

The pinned paper's ACS subsection states that active sampling's roughly 60% labeling-budget reduction is relative to **classical**. In the same experiments section, the paper separately defines:

- **classical:** an IPW U-statistic with uniform sampling;
- **uniform:** an AIPW U-statistic with uniform sampling.

They therefore share a sampling policy but are distinct estimators. The ACS text names the uniform baseline but does not state the same 60% figure relative to it.

## Result

**Falsified — literal comparator attribution.** The live claim assigns the paper's roughly 60% result to uniform sampling, whereas the primary source explicitly assigns it to the distinct classical estimator. This conclusion is limited to the wording/comparator mismatch; the unreleased ACS protocol still prevents a source-faithful numerical rerun or a claim about any unreported active-versus-uniform effect.

## Reproduction

```bash
.venv/bin/python src/claim4_falsification_comparator_audit.py
.venv/bin/python -m pytest -q
sha256sum -c outputs/claim4_falsification_SHA256SUMS
```

## Retained artifacts

- `outputs/claim4_falsification_result.json`
- `outputs/claim4_falsification_test.log`
- `outputs/claim4_falsification_SHA256SUMS`
- pinned source: `upstream/arxiv_source/ICML_Camera-ready.tex`
