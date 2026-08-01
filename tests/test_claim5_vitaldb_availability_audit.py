import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_claim5_attempt1_is_protocol_audit_not_proxy():
    subprocess.run([sys.executable, "src/claim5_vitaldb_availability_audit.py"], cwd=ROOT, check=True)
    result = json.loads((ROOT / "outputs/claim5_attempt1_result.json").read_text())
    assert result["claim"] == 5
    assert result["attempt"] == 1
    assert result["outcome"] == "inconclusive"
    assert result["source_faithful_rerun_possible"] is False
    assert all(result["source_checks"].values())
    assert len(result["blockers"]) >= 5
    assert "proxy" in result["scope"]
