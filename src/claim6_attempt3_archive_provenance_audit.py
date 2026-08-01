#!/usr/bin/env python3
"""Claim 6 Attempt 3: independent archive/dataset-provenance availability audit."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream" / "arxiv_source"
EVIDENCE = ROOT / "evidence" / "claim6_attempt3"
OUT = ROOT / "outputs" / "claim6_attempt3"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    tex = (SOURCE / "ICML_Camera-ready.tex").read_text()
    inventory = (EVIDENCE / "arxiv_source_inventory.txt").read_text().splitlines()
    prior_metadata = (EVIDENCE / "arxiv_prior_work_query.xml").read_text()
    title_search = json.loads((EVIDENCE / "github_title_search.json").read_text())
    code_status = (EVIDENCE / "github_code_search_status.txt").read_text().strip()

    executable_or_data = [
        item for item in inventory
        if Path(item).suffix.lower() in {".py", ".r", ".ipynb", ".csv", ".tsv", ".parquet", ".jsonl", ".pkl", ".yaml", ".yml"}
    ]
    facts = {
        "selected_source_has_political_protocol": "Political bias dataset" in tex,
        "selected_source_declares_3000_trials": "averaged over 3000 trials" in tex,
        "selected_source_declares_gpt35_and_gpt4": "predictions of GPT-3.5" in tex and "predictions from GPT-4" in tex,
        "selected_source_releases_no_data_or_code": not executable_or_data,
        "prior_work_arxiv_record_exists": "Can Unconfident LLM Annotations Be Used for Confident Conclusions?" in prior_metadata,
        "prior_work_metadata_mentions_bias_setting": "bias" in prior_metadata.lower(),
        "selected_title_github_repo_count": title_search["total_count"],
        "unauthenticated_github_code_search_http_status": code_status,
    }
    if not all([facts["selected_source_has_political_protocol"], facts["selected_source_declares_3000_trials"], facts["selected_source_declares_gpt35_and_gpt4"], facts["selected_source_releases_no_data_or_code"], facts["prior_work_arxiv_record_exists"]]):
        raise SystemExit(f"expected archival facts missing: {facts}")
    if facts["selected_title_github_repo_count"] != 0:
        raise SystemExit("unexpected selected-paper GitHub repository discovery")

    OUT.mkdir(parents=True, exist_ok=True)
    result = {
        "claim": 6,
        "attempt": 3,
        "outcome": "inconclusive",
        "scope": "independent arXiv-archive and dataset-provenance audit; no proxy political-bias run",
        "source_faithful_rerun_possible": False,
        "evidence_hashes": {path.name: digest(path) for path in sorted(EVIDENCE.iterdir()) if path.is_file() and path.name != "SHA256SUMS"},
        "facts": facts,
        "selected_source_executable_or_data_assets": executable_or_data,
        "blockers": [
            "The selected accepted source documents GPT-3.5/GPT-4 labels and 3,000 trials but releases no data, executable, configuration, seed, or trial-output asset.",
            "The authoritative prior-work arXiv record establishes related bias-setting provenance, not a selected-paper snapshot, paper-era LLM outputs, or selected-paper protocol.",
            "No exact-title selected-paper GitHub repository was found in the retained API response; anonymous GitHub code search was rate/auth restricted (HTTP 401), so it cannot establish a released dataset path.",
        ],
        "next_action": "claim_6_falsification_literal_source_scope",
    }
    (OUT / "result.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
