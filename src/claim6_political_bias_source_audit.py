#!/usr/bin/env python3
"""CPU-only source/protocol audit for live Claim 6 (political-bias Kendall tau).

This audit verifies the accepted paper's stated target, comparators, and
reported savings from the pinned TeX source.  It deliberately does not claim a
numerical reproduction: the source package has no political-bias records, LLM
labels, model/configuration, seed, or trial-result artifacts.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream" / "arxiv_source"
TEX = SOURCE / "ICML_Camera-ready.tex"
README = SOURCE / "00README.json"
OUT_DIR = ROOT / "outputs" / "claim6_attempt1"
OUT = OUT_DIR / "result.json"
INVENTORY = OUT_DIR / "source_asset_inventory.txt"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def line_number(text: str, needle: str) -> int:
    for number, line in enumerate(text.splitlines(), start=1):
        if needle in line:
            return number
    raise ValueError(f"missing source phrase: {needle}")


def main() -> None:
    tex = TEX.read_text()
    files = sorted(path.relative_to(SOURCE).as_posix() for path in SOURCE.rglob("*") if path.is_file())
    executable_or_data_suffixes = {".py", ".r", ".ipynb", ".csv", ".tsv", ".parquet", ".xlsx", ".pkl", ".joblib", ".yaml", ".yml"}
    protocol_assets = [name for name in files if Path(name).suffix.lower() in executable_or_data_suffixes]

    facts = {
        "political_bias_task": "political-bias} task" in tex,
        "kendall_target": "Kendall's $\\tau$ coefficient" in tex,
        "ordinal_agreement_kernel": "\\mathrm{sign}\\!\\Big((Y_1^{\\rm TR}-Y_2^{\\rm TR})" in tex,
        "gpt35_predictor": "predictions of GPT-3.5" in tex,
        "gpt4_uncertainty": "predictions from GPT-4" in tex,
        "classical_twenty_percent": "about 20\\% less budget than {classical} baseline" in tex,
        "uniform_ten_percent": "about 10\\% less budget than {uniform} sampling" in tex,
        "three_thousand_trials": "averaged over 3000 trials" in tex,
        "figure_asset": "Figure/combined_kendall.pdf" in files,
    }
    if not all(facts.values()):
        raise SystemExit(f"missing expected political-bias facts: {facts}")
    if protocol_assets:
        raise SystemExit(f"unexpected executable/data asset(s): {protocol_assets}")

    # Meaningful literal-comparator negative control: the source separately
    # assigns 20% to classical and 10% to uniform.  Swapping these labels must
    # fail this source-backed control rather than silently treating baselines as
    # interchangeable.
    swapped_comparator_claim_supported = (
        "about 20\\% less budget than {uniform} sampling" in tex
        or "about 10\\% less budget than {classical} baseline" in tex
    )
    if swapped_comparator_claim_supported:
        raise SystemExit("unexpected swapped comparator wording in source")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    INVENTORY.write_text("\n".join(files) + "\n")
    result = {
        "claim": 6,
        "attempt": 1,
        "outcome": "inconclusive",
        "scope": "accepted-source protocol/comparator audit only; no political-bias numerical rerun",
        "source_tex_sha256": sha256(TEX),
        "source_readme_sha256": sha256(README),
        "source_archive_sha256": sha256(ROOT / "evidence" / "arxiv_source.tar"),
        "source_asset_inventory_sha256": sha256(INVENTORY),
        "source_file_count": len(files),
        "figure_assets": [name for name in files if name.startswith("Figure/")],
        "executable_or_data_assets": protocol_assets,
        "source_facts": facts,
        "source_lines": {
            "task_and_figure": line_number(tex, "Political bias dataset"),
            "kendall_target": line_number(tex, "Kendall's $\\tau$ coefficient"),
            "reported_savings": line_number(tex, "about 20\\% less budget than {classical} baseline"),
            "trial_protocol": line_number(tex, "averaged over 3000 trials"),
        },
        "negative_control": {
            "name": "swapped_classical_uniform_comparator",
            "swapped_source_wording_supported": swapped_comparator_claim_supported,
            "interpretation": "The source supports 20% versus classical and 10% versus uniform; it does not support swapping those comparator-specific numbers.",
        },
        "source_faithful_rerun_possible": False,
        "blockers": [
            "The accepted source package contains no political-bias article records, ground-truth labels, GPT-3.5 proxy labels, GPT-4 uncertainty outputs, split, or paper-era data snapshot.",
            "The source reports 3,000 trials but releases no estimator implementation, sampling/configuration details, seeds, budget-to-precision interpolation, or trial outputs.",
            "The published Kendall figure is an output asset, not executable evidence sufficient to regenerate the claimed budget savings.",
        ],
        "next_action": "claim_6_attempt_2_authoritative_dataset_and_author_release_search",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
