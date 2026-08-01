"""Primary ACS provenance audit for Claim 4 Attempt 3.

This is an availability certificate, not an ACS proxy experiment.  It compares
archived Census PUMS release directories and the paper's own ACS section to
establish whether the exact reported protocol is reconstructable.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream" / "arxiv_source" / "ICML_Camera-ready.tex"
EVIDENCE = ROOT / "evidence" / "claim4_attempt3"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def calculate() -> dict:
    source = SOURCE.read_text(encoding="utf-8")
    section = source[source.index("\\subsection{Income dataset (ACS)}") : source.index("\\begin{figure*}", source.index("\\subsection{Income dataset (ACS)}"))]
    rows = [line.split("\t") for line in (EVIDENCE / "retrieval.tsv").read_text().splitlines()]
    statuses = {url: status for status, url, _ in rows}
    release_2023 = EVIDENCE / "response_3.html"
    release_2022 = EVIDENCE / "response_4.html"
    required_missing = [
        "ACS/PUMS release year and 1-year/5-year product",
        "geographic extraction and row eligibility filters",
        "income target transformation and feature encoding",
        "train/auxiliary/test split and random seeds",
        "XGBoost and proxy-model hyperparameters",
        "active/classical/uniform replicate-level results",
    ]
    return {
        "audit_type": "independent_primary_acs_archive_and_source_protocol_availability",
        "census_primary_records": {
            "microdata_page_http_status": statuses["https://www.census.gov/programs-surveys/acs/microdata.html"],
            "pums_2023_1_year_directory_http_status": statuses["https://www2.census.gov/programs-surveys/acs/data/pums/2023/1-Year/"],
            "pums_2022_1_year_directory_http_status": statuses["https://www2.census.gov/programs-surveys/acs/data/pums/2022/1-Year/"],
            "distinct_2022_2023_archive_listing_hashes": digest(release_2022) != digest(release_2023),
        },
        "paper_acs_section": {
            "identifies_acs_and_income_target": "American Community Survey (ACS)" in section and "income label" in section,
            "states_xgboost_for_prediction_and_proxy": "XGBoost" in section,
            "explicitly_names_60_percent_comparator": "60\\% labeling-budget reduction relative to {classical}" in section,
            "explicitly_names_uniform_60_percent_comparator": "60\\% labeling-budget reduction relative to {uniform}" in section,
            "required_protocol_fields_not_specified": required_missing,
        },
        "source_faithful_cpu_run_executed": False,
        "verdict": "inconclusive_source_artifact_scope",
        "reason": (
            "Official Census records expose distinct ACS/PUMS release archives, but the paper's ACS section does not identify a release, extraction, transformation, split, seed, model configuration, or replicate outputs. "
            "The source explicitly attaches roughly 60% reduction to the classical baseline and does not state that same number relative to uniform. "
            "An ACS proxy would therefore not resolve the live uniform-comparison claim."
        ),
        "next_action": "claim_4_falsification_literal_uniform_comparator_source_scope",
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2, sort_keys=True))
