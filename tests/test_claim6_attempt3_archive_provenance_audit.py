from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_claim6_attempt3_retains_archive_and_dataset_provenance_limits() -> None:
    subprocess.run(["python3", "src/claim6_attempt3_archive_provenance_audit.py"], cwd=ROOT, check=True)
    result = json.loads((ROOT / "outputs" / "claim6_attempt3" / "result.json").read_text())
    assert result["claim"] == 6
    assert result["attempt"] == 3
    assert result["outcome"] == "inconclusive"
    assert result["source_faithful_rerun_possible"] is False
    assert result["facts"]["selected_source_releases_no_data_or_code"] is True
    assert result["facts"]["prior_work_arxiv_record_exists"] is True
    assert result["facts"]["selected_title_github_repo_count"] == 0
