#!/usr/bin/env python3
"""Attempt-3 source-asset audit for the VitalDB Claim-5 experiment.

This is deliberately an archival/provenance audit, not a reconstructed clinical
experiment. It establishes which parts of the published protocol are present in
the accepted arXiv source package and which reproducibility-critical artifacts
are absent from that package.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream" / "arxiv_source"
TEX = SOURCE / "ICML_Camera-ready.tex"
README = SOURCE / "00README.json"
OUT_DIR = ROOT / "outputs" / "claim5_attempt3"
OUT = OUT_DIR / "result.json"
INVENTORY = OUT_DIR / "source_asset_inventory.txt"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    tex = TEX.read_text()
    files = sorted(path.relative_to(SOURCE).as_posix() for path in SOURCE.rglob("*") if path.is_file())
    INVERSE_PROTOCOL_ARTIFACT_SUFFIXES = {".py", ".r", ".ipynb", ".csv", ".tsv", ".parquet", ".xlsx", ".pkl", ".joblib", ".yaml", ".yml"}
    protocol_assets = [name for name in files if Path(name).suffix.lower() in INVERSE_PROTOCOL_ARTIFACT_SUFFIXES]
    figure_assets = [name for name in files if name.startswith("Figure/")]

    source_facts = {
        "vitaldb_cases": "records from 6,388 surgical cases" in tex,
        "hemoglobin_window": "within a $\\pm 24$ hour window around $t_0$" in tex,
        "paired_outcome": "D=Y^{a}-Y^{b}" in tex,
        "xgboost": "implemented using XGBoost" in tex,
        "three_thousand_trials": "averaged over 3000 trials" in tex,
        "claimed_twenty_percent": "about 20\\% fewer labels than {classical} baseline" in tex,
        "figure_reference": "Figure/combined_wilcoxon.pdf" in tex,
    }
    if not all(source_facts.values()):
        raise SystemExit(f"required VitalDB source facts missing: {source_facts}")
    if protocol_assets:
        raise SystemExit(f"source package unexpectedly contains executable/data artifacts: {protocol_assets}")
    if "Figure/combined_wilcoxon.pdf" not in figure_assets:
        raise SystemExit("published VitalDB figure asset missing")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    INVENTORY.write_text("\n".join(files) + "\n")
    payload = {
        "claim": 5,
        "attempt": 3,
        "outcome": "inconclusive",
        "scope": "accepted arXiv source-package/archival asset audit only; no proxy VitalDB cohort or numerical rerun",
        "source_tex_sha256": sha256(TEX),
        "source_readme_sha256": sha256(README),
        "source_archive_sha256": sha256(ROOT / "evidence" / "arxiv_source.tar"),
        "source_asset_inventory_sha256": sha256(INVENTORY),
        "source_file_count": len(files),
        "figure_assets": figure_assets,
        "executable_or_data_assets": protocol_assets,
        "source_facts": source_facts,
        "author_release_history_evidence": {
            "attempt_2_exact_title_repositories": "evidence/claim5_attempt2/repos_exact.json",
            "attempt_2_author_repositories": "evidence/claim5_attempt2/repos_authors.json",
            "attempt_2_virtual_paper": "evidence/claim5_attempt2/icml_virtual.html",
            "finding": "retained prior authoritative author/history records contain no executable or supplement; this attempt does not repeat those network searches"
        },
        "vitaldb_archival_evidence": {
            "attempt_1_manifest": "evidence/claim5_attempt1/retrieval.tsv",
            "finding": "retained official VitalDB endpoint captures identify current access APIs, not the accepted snapshot, selected-case manifest, paper-era preprocessing, or trial outputs"
        },
        "source_faithful_rerun_possible": False,
        "blockers": [
            "Accepted source package contains TeX, styles, bibliography, and figure PDFs but no executable, data snapshot, case manifest, model serialization, seed/configuration, or trial-output artifact.",
            "The source describes the cohort/window/outcome and reports the 20% result but omits selected case IDs, covariate preprocessing, XGBoost hyperparameters, pilot/fold assignment, active-sampling seeds, and 3,000-run outputs.",
            "Retained official VitalDB and author/history evidence from distinct prior attempts does not close those missing inputs."
        ],
        "next_action": "claim_5_falsification_attempt_literal_source/protocol scope audit; do not run a proxy VitalDB experiment"
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
