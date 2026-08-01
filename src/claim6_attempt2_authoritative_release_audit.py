#!/usr/bin/env python3
"""Claim 6 Attempt 2: audit authoritative author/dataset/release evidence.

This deliberately distinguishes the selected paper from the earlier public
Robust Active Statistical Inference repository cited by the selected paper.
The latter is useful provenance, but its different GPT-4o notebook and absent
`data/bias_dataset.csv` cannot reproduce the selected paper's GPT-3.5/GPT-4,
3,000-trial result.
"""
from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence" / "claim6_attempt2"
OUT = ROOT / "outputs" / "claim6_attempt2"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: str):
    return json.loads((EVIDENCE / path).read_text())


def main() -> None:
    # GitHub exact-title searches: selected paper and its exact title produce
    # no repository. The public prior-work repository is preserved separately.
    selected_search = load("response_1")
    prior_search = load("response_3")
    repository = load("response_10.json")
    tree = load("response_14.json")["tree"]
    notebook_api = load("response_20.json")
    notebook = base64.b64decode(notebook_api["content"]).decode(errors="replace")
    paths = [entry["path"] for entry in tree]

    facts = {
        "selected_title_repository_count": selected_search["total_count"],
        "prior_work_repository": repository["full_name"],
        "prior_work_search_count": prior_search["total_count"],
        "prior_work_has_bias_notebook": "bias.ipynb" in paths,
        "prior_work_has_bias_data": any(path.endswith("bias_dataset.csv") for path in paths),
        "prior_notebook_expects_untracked_bias_csv": "data/bias_dataset.csv" in notebook,
        "prior_notebook_uses_gpt4o": "label_gpt4o" in notebook,
        "prior_notebook_uses_selected_gpt35": "GPT-3.5" in notebook or "gpt-3.5" in notebook.lower(),
        "prior_repo_has_selected_paper_trial_outputs": any("3000" in path.lower() or "trial" in path.lower() for path in paths),
    }
    if facts["selected_title_repository_count"] != 0:
        raise SystemExit("unexpected exact-title repository discovery")
    if facts["prior_work_repository"] != "lphLeo/Robust-Active-Statistical-Inference":
        raise SystemExit("prior-work repository identity changed")
    if not facts["prior_work_has_bias_notebook"] or not facts["prior_notebook_expects_untracked_bias_csv"]:
        raise SystemExit("expected provenance distinction is missing")
    if facts["prior_work_has_bias_data"] or facts["prior_notebook_uses_selected_gpt35"]:
        raise SystemExit("prior repository unexpectedly contains selected-paper assets")

    OUT.mkdir(parents=True, exist_ok=True)
    inventory = OUT / "prior_work_tree.txt"
    inventory.write_text("\n".join(paths) + "\n")
    result = {
        "claim": 6,
        "attempt": 2,
        "outcome": "inconclusive",
        "scope": "authoritative GitHub/related-release availability audit; no proxy political-bias run",
        "evidence_hashes": {name: digest(EVIDENCE / name) for name in [
            "response_1", "response_3", "response_10.json", "response_14.json", "response_20.json", "retrieval.tsv"
        ]},
        "prior_work_tree_sha256": digest(inventory),
        "facts": facts,
        "source_faithful_rerun_possible": False,
        "blockers": [
            "No exact-title GitHub repository for the selected paper was found in the retained GitHub API search.",
            "The only relevant public prior-work repository is not an author release of this selected paper and uses a different GPT-4o notebook, while the selected paper specifies GPT-3.5 predictions and GPT-4 uncertainty.",
            "That prior notebook requires an untracked data/bias_dataset.csv, and its repository tree contains no selected-paper snapshot, LLM outputs, configuration, seeds, 3,000-trial results, or generated Figure 3 data.",
        ],
        "next_action": "claim_6_attempt_3_authoritative_archive_and_dataset_provenance_audit",
    }
    (OUT / "result.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
