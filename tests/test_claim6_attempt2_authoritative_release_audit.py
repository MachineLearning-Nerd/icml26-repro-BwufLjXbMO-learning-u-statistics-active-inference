from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_claim6_attempt2_distinguishes_prior_release_from_selected_protocol() -> None:
    subprocess.run(["python3", "src/claim6_attempt2_authoritative_release_audit.py"], cwd=ROOT, check=True)
    result = json.loads((ROOT / "outputs" / "claim6_attempt2" / "result.json").read_text())
    assert result["claim"] == 6
    assert result["attempt"] == 2
    assert result["outcome"] == "inconclusive"
    assert result["source_faithful_rerun_possible"] is False
    facts = result["facts"]
    assert facts["selected_title_repository_count"] == 0
    assert facts["prior_work_repository"] == "lphLeo/Robust-Active-Statistical-Inference"
    assert facts["prior_notebook_expects_untracked_bias_csv"] is True
    assert facts["prior_notebook_uses_gpt4o"] is True
    assert facts["prior_notebook_uses_selected_gpt35"] is False
