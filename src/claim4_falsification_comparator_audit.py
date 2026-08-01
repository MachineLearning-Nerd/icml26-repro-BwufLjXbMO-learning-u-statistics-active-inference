"""Literal comparator-scope audit for live Claim 4.

This checks the challenge wording against the pinned primary paper.  It does not
claim an ACS rerun or infer an unreported numerical active-vs-uniform result.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream" / "arxiv_source" / "ICML_Camera-ready.tex"


def income_section(text: str) -> str:
    start = text.index("\\subsection{Income dataset (ACS)}")
    end = text.index("\\begin{figure*}", start)
    return text[start:end]


def experiment_baselines(text: str) -> str:
    start = text.index("\\section{Experiments}")
    end = text.index("\\subsection{Income dataset (ACS)}", start)
    return text[start:end]


def calculate() -> dict:
    text = SOURCE.read_text(encoding="utf-8")
    acs = income_section(text)
    baselines = experiment_baselines(text)
    exact_classical = "roughly a 60\\% labeling-budget reduction relative to {classical} one"
    exact_uniform = "roughly a 60\\% labeling-budget reduction relative to {uniform}"
    classical_definition = "The IPW $U$-statistic with uniform sampling"
    uniform_definition = "The AIPW $U$-statistic $U_{\\mathrm{AIPW}}^{\\pi}"

    return {
        "audit_type": "literal_live_claim_comparator_scope",
        "live_claim_comparator": "uniform sampling",
        "source_acs_60_percent_statement": exact_classical,
        "source_facts": {
            "exact_60_percent_relative_to_classical": exact_classical in acs,
            "exact_60_percent_relative_to_uniform": exact_uniform in acs,
            "acs_section_mentions_uniform_baseline": "{uniform} baselines" in acs,
            "classical_is_ipw_under_uniform_sampling": classical_definition in baselines,
            "uniform_is_aipw_under_uniform_sampling": uniform_definition in baselines,
            "methods_are_distinct_despite_same_sampling_policy": (
                classical_definition in baselines and uniform_definition in baselines
            ),
        },
        "scope": (
            "The conclusion concerns the literal source attribution of the 60% "
            "number, not whether an unreported active-vs-uniform numerical result "
            "could hold under another experiment."
        ),
        "verdict": "falsified_literal_comparator_attribution",
        "reason": (
            "The pinned ACS text explicitly attributes roughly 60% budget reduction "
            "to the classical estimator. The paper separately defines uniform as a "
            "different AIPW estimator under the same uniform sampling policy and does "
            "not attach the 60% statement to it. Thus 'roughly 60% relative to uniform' "
            "is not a defensible reading of the cited source claim."
        ),
        "source_faithful_acs_rerun_executed": False,
        "next_action": "claim_5_attempt_1_vitaldb_source_protocol_audit",
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2, sort_keys=True))
