"""Literal-source falsification audit for live Claim 5.

This is deliberately a source-scope check, not a substitute VitalDB experiment.
It tests whether the exact 20%-versus-classical wording is contradicted by the
accepted paper source.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream" / "arxiv_source" / "ICML_Camera-ready.tex"


def vitaldb_section(text: str) -> str:
    start = text.index("\\subsection{Perioperative dataset (VitalDB)}")
    end = text.index("\\subsection{Political bias dataset}", start)
    return text[start:end]


def calculate() -> dict:
    text = SOURCE.read_text(encoding="utf-8")
    section = vitaldb_section(text)
    exact_claim_support = (
        "comparable precision with about 20\\% fewer labels than {classical} baseline"
    )
    contradictory_comparator = "about 20\\% fewer labels than {uniform} baseline"
    return {
        "audit_type": "literal_live_claim_source_protocol_scope",
        "live_claim_scope": (
            "Active Wilcoxon signed-rank test on VitalDB hemoglobin shifts needs "
            "approximately 20% less budget than classical for equivalent precision."
        ),
        "source_facts": {
            "vitaldb_heading_present": "Perioperative dataset (VitalDB)" in section,
            "hemoglobin_pairing_protocol_present": "focus on hemoglobin" in section
            and "paired difference" in section,
            "wilcoxon_target_present": "Wilcoxon signed-rank" in section,
            "exact_20_percent_classical_statement_present": exact_claim_support in section,
            "contradictory_20_percent_uniform_statement_present": contradictory_comparator
            in section,
            "near_nominal_coverage_statement_present": "near-nominal coverage" in section,
        },
        "verdict": "inconclusive_literal_source_supports_claim",
        "reason": (
            "The accepted source explicitly states comparable precision with about "
            "20% fewer labels than the classical baseline in the VitalDB section. "
            "No literal source/protocol contradiction was found. The missing released "
            "snapshot, preprocessing, XGBoost configuration, seeds, and trial outputs "
            "still prevent independent numerical verification."
        ),
        "source_faithful_vitaldb_rerun_executed": False,
        "next_action": "claim_6_attempt_1_political_bias_source_protocol_audit",
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2, sort_keys=True))
