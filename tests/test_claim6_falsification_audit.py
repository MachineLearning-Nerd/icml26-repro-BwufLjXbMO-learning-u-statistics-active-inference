from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_claim6_literal_source_falsification_is_inconclusive() -> None:
    subprocess.run(["python3", "src/claim6_falsification_audit.py"], cwd=ROOT, check=True)
    result = json.loads((ROOT / "outputs" / "claim6_falsification_result.json").read_text())
    assert result["claim"] == 6
    assert result["attempt"] == "falsification"
    assert result["outcome"] == "inconclusive"
    assert result["checks"]["source_sentence_present"] is True
    assert result["checks"]["source_does_not_swap_comparators"] is True
