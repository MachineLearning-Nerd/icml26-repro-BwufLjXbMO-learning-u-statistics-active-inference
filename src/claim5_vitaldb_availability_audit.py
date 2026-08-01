#!/usr/bin/env python3
"""Audit whether the released VitalDB material supports Claim 5 reproduction.

This intentionally does not construct a proxy clinical cohort or report a
numerical reproduction.  It records only source-pinned protocol facts and
availability blockers required for a source-faithful rerun.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "upstream/arxiv_source/ICML_Camera-ready.tex"
RETRIEVAL = ROOT / "evidence/claim5_attempt1/retrieval.tsv"
OUT = ROOT / "outputs/claim5_attempt1_result.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    tex = TEX.read_text()
    retrieval = RETRIEVAL.read_text()
    required_source_phrases = {
        "cohort": "records from 6,388 surgical cases",
        "event_and_window": "within a $\\pm 24$ hour window around $t_0$",
        "outcome": "D=Y^{a}-Y^{b}",
        "models": "implemented using XGBoost",
        "budget_comparator": "about 20\\% fewer labels than {classical} baseline and 10\\% fewer than uniform sampling",
        "trials": "averaged over 3000 trials",
        "perioperative_labels": "m_{\\text{Perioperative}}=760",
    }
    source_checks = {name: phrase in tex for name, phrase in required_source_phrases.items()}
    # The API/document URLs were retrieved, but the paper provides no executable,
    # accepted-data snapshot, selected-case IDs, XGBoost configuration, fixed
    # random seeds, or trial outputs.  Those omissions prevent a faithful run.
    blockers = [
        "No author executable repository or experiment runner is present in the pinned arXiv source.",
        "No accepted VitalDB snapshot/version, download manifest, or selected case identifiers are specified.",
        "No case-level covariate schema/preprocessing or XGBoost hyperparameters are released.",
        "No active-sampling initial query set, budget-to-label mapping, sampling random seeds, or 3000 trial outputs are released.",
        "VitalDB dataset access is governed by the retrieved data-use agreement; this audit did not obtain or redistribute clinical data.",
    ]
    payload = {
        "claim": 5,
        "attempt": 1,
        "outcome": "inconclusive",
        "scope": "source/protocol/data availability audit only; no VitalDB proxy or numerical reproduction was run",
        "source_checks": source_checks,
        "source_tex_sha256": sha256(TEX),
        "retrieval_manifest_sha256": sha256(RETRIEVAL),
        "retrieved_endpoints": retrieval.strip().splitlines(),
        "public_data_license_observation": "Retrieved VitalDB data-use agreement states CC BY-NC-SA 4.0, subject to its terms.",
        "source_faithful_rerun_possible": False,
        "blockers": blockers,
        "next_action": "claim_5_attempt_2_search_official VitalDB version history and author supplement/code for the omitted protocol artifacts",
    }
    if not all(source_checks.values()):
        raise SystemExit(f"missing pinned source protocol phrases: {source_checks}")
    OUT.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
