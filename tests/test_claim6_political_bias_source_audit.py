from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_claim6_political_bias_source_protocol_audit() -> None:
    subprocess.run(["python3", "src/claim6_political_bias_source_audit.py"], cwd=ROOT, check=True)
    result = json.loads((ROOT / "outputs" / "claim6_attempt1" / "result.json").read_text())
    assert result["claim"] == 6
    assert result["attempt"] == 1
    assert result["outcome"] == "inconclusive"
    assert result["source_faithful_rerun_possible"] is False
    assert result["source_facts"]["classical_twenty_percent"] is True
    assert result["source_facts"]["uniform_ten_percent"] is True
    assert result["negative_control"]["swapped_source_wording_supported"] is False
    assert result["executable_or_data_assets"] == []
