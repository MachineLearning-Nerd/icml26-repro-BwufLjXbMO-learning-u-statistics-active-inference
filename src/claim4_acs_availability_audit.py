"""Source-availability audit for Claim 4; this is not an ACS reproduction."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream" / "arxiv_source" / "ICML_Camera-ready.tex"


def calculate() -> dict:
    text = SOURCE.read_text(encoding="utf-8")
    source_files = sorted(
        str(path.relative_to(ROOT / "upstream" / "arxiv_source"))
        for path in (ROOT / "upstream" / "arxiv_source").rglob("*")
        if path.is_file()
    )
    # Source-faithful execution needs data plus the experiment implementation,
    # preprocessing, XGBoost parameters, and sampling seeds.  The retained
    # arXiv source contains TeX and rendered figures only.
    absent_required = {
        "ACS/Folktables dataset snapshot or retrieval version": True,
        "income target/preprocessing and train/test split": True,
        "XGBoost hyperparameters and random seeds": True,
        "active/classical/uniform experiment runner": True,
        "per-trial estimates/coverage/effective-sample-size outputs": True,
    }
    return {
        "audit_type": "source_and_protocol_availability_only",
        "source_facts": {
            "acs_named": "American Community Survey (ACS)" in text,
            "income_label_named": "label $Y$ represents the income measure" in text,
            "xgboost_named": "implemented using XGBoost" in text,
            "budget_values_named": "n_b\\in\\{800,4800,8800,12000,16000\\}" in text,
            "target_coverage_named": "target coverage level 90\\%" in text,
            "reported_60_percent_wording": "roughly a 60\\% labeling-budget reduction" in text,
            "reported_trials": "averaged over 3000 trials" in text,
            "income_labeled_sample_count": "m_{\\text{Income}}=1000" in text,
            "runtime_setup_named": "n=80{,}000" in text,
        },
        "retained_source_files": source_files,
        "required_inputs_absent_from_retained_release": absent_required,
        "source_faithful_cpu_run_executed": False,
        "verdict": "inconclusive_source_artifact_scope",
        "reason": (
            "The paper specifies high-level ACS/Gini, budget, XGBoost, and "
            "3000-trial details, but the pinned public arXiv release contains "
            "no executable code, ACS snapshot/version, preprocessing/split, "
            "hyperparameters/seeds, or trial outputs. A substitute ACS run "
            "would be a proxy, not a reproduction of the reported 60% and "
            "90% claims."
        ),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(calculate(), indent=2, sort_keys=True))
