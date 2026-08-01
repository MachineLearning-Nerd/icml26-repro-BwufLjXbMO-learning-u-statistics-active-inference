from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_claim5_attempt3_archival_asset_audit() -> None:
    subprocess.run(["python3", "src/claim5_attempt3_source_asset_audit.py"], cwd=ROOT, check=True)
    result = json.loads((ROOT / "outputs/claim5_attempt3/result.json").read_text())
    assert result["attempt"] == 3
    assert result["outcome"] == "inconclusive"
    assert result["source_faithful_rerun_possible"] is False
    assert result["source_facts"]["claimed_twenty_percent"] is True
    assert result["source_facts"]["three_thousand_trials"] is True
    assert result["executable_or_data_assets"] == []
    assert "Figure/combined_wilcoxon.pdf" in result["figure_assets"]
