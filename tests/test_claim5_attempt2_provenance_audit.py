import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_attempt2_retains_an_availability_not_proxy_verdict():
    subprocess.run(
        ["python", "src/claim5_attempt2_provenance_audit.py"], cwd=ROOT, check=True
    )
    result = json.loads((ROOT / "outputs/claim5_attempt2_result.json").read_text())
    assert result["claim"] == 5
    assert result["attempt"] == 2
    assert result["outcome"] == "inconclusive"
    assert result["source_faithful_rerun_possible"] is False
    assert all(result["source_checks"].values())
    assert result["exact_title_repository_search_total"] == 0
    assert result["author_query_repository_search_total"] == 0
    assert "proxy clinical cohort" in result["scope"]
