#!/usr/bin/env python3
"""Attempt-2 provenance audit for the VitalDB Claim-5 protocol.

This checks retained official/author-discovery responses and the pinned paper
source. It deliberately does not substitute a newly constructed VitalDB cohort
for the unreleased paper-era experiment.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "upstream/arxiv_source/ICML_Camera-ready.tex"
EVIDENCE = ROOT / "evidence/claim5_attempt2"
OUT = ROOT / "outputs/claim5_attempt2_result.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(name: str) -> dict:
    return json.loads((EVIDENCE / name).read_text())


def main() -> None:
    tex = TEX.read_text()
    exact_repo = load_json("repos_exact.json")
    author_repo = load_json("repos_authors.json")
    code_hits = load_json("github_code_exact.json")
    virtual = (EVIDENCE / "icml_virtual.html").read_text(errors="replace").lower()
    retrieval = (EVIDENCE / "retrieval.tsv").read_text()

    source_checks = {
        "cohort": "records from 6,388 surgical cases" in tex,
        "window": "within a $\\pm 24$ hour window around $t_0$" in tex,
        "xgboost": "implemented using XGBoost" in tex,
        "trials": "averaged over 3000 trials" in tex,
        "comparison": "about 20\\% fewer labels than {classical} baseline" in tex,
    }
    # Exact-title repository searches find none. Code search necessarily finds
    # this reproduction repo, so it is evidence only after author/reproduction
    # index entries are excluded rather than a claim that GitHub has no hits.
    non_reproduction_code_hits = [
        item.get("html_url", "")
        for item in code_hits.get("items", [])
        if "MachineLearning-Nerd/icml26-repro-BwufLjXbMO" not in item.get("html_url", "")
        and "Auto-Arxiv-Subscription" not in item.get("html_url", "")
    ]
    supplement_markers = ["supplement", "github.com", "code release"]
    payload = {
        "claim": 5,
        "attempt": 2,
        "outcome": "inconclusive",
        "scope": "official VitalDB/history and author-release availability audit only; no proxy clinical cohort or numerical claim reproduction",
        "source_checks": source_checks,
        "source_tex_sha256": digest(TEX),
        "retrieval_manifest_sha256": digest(EVIDENCE / "retrieval.tsv"),
        "exact_title_repository_search_total": exact_repo.get("total_count"),
        "author_query_repository_search_total": author_repo.get("total_count"),
        "non_reproduction_code_hits": non_reproduction_code_hits,
        "virtual_page_has_release_marker": {marker: marker in virtual for marker in supplement_markers},
        "retrieved_endpoints": retrieval.strip().splitlines(),
        "source_faithful_rerun_possible": False,
        "blockers": [
            "No exact-title author repository was returned by retained GitHub repository searches.",
            "The official virtual-paper page supplies the abstract but no retained supplement/code-release marker.",
            "The retained VitalDB pages/API responses identify current access endpoints, not the accepted snapshot, selected 6,388-case cohort, or paper-era extraction manifest.",
            "The pinned source still omits case identifiers, covariate preprocessing, XGBoost hyperparameters, fold/pilot construction, active-sampling seeds, and 3,000 trial outputs.",
        ],
        "next_action": "claim_5_attempt_3_search_archived author/repository release history and paper-source assets; only run CPU protocol if all missing source-faithful inputs are recovered",
    }
    if not all(source_checks.values()):
        raise SystemExit(f"missing source facts: {source_checks}")
    if exact_repo.get("total_count") != 0 or author_repo.get("total_count") != 0:
        raise SystemExit("repository search result changed; inspect before retaining an availability conclusion")
    OUT.write_text(json.dumps(payload, indent=2) + "\n")


if __name__ == "__main__":
    main()
