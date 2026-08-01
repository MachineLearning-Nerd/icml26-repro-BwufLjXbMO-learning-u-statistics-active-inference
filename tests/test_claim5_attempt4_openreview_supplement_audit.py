from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_claim5_attempt4_openreview_access_audit() -> None:
    subprocess.run(["python3", "src/claim5_attempt4_openreview_supplement_audit.py"], cwd=ROOT, check=True)
    result = json.loads((ROOT / "outputs/claim5_attempt4/result.json").read_text())
    assert result["attempt"] == 4
    assert result["outcome"] == "inconclusive"
    assert result["forum_http_status"] == "200"
    assert result["forum_turnstile_present"] is True
    assert result["api_http_statuses"] == ["403", "403"]
    assert result["source_faithful_rerun_possible"] is False
