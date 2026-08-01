"""Authoritative-material provenance audit for Claim 4 Attempt 2.

This checks retained responses from the official paper records and GitHub's public
repository search. It intentionally does not treat an unreleased ACS proxy as a
paper-faithful reproduction.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "upstream" / "arxiv_source" / "ICML_Camera-ready.tex"
EVIDENCE = ROOT / "evidence" / "claim4_attempt2"


def calculate() -> dict:
    source = SOURCE.read_text(encoding="utf-8")
    records = (EVIDENCE / "retrieval.tsv").read_text(encoding="utf-8")
    title_search = json.loads((EVIDENCE / "response_4").read_text(encoding="utf-8"))
    aipw_search = json.loads((EVIDENCE / "response_5").read_text(encoding="utf-8"))
    arxiv_page = (EVIDENCE / "response_3").read_text(encoding="utf-8")
    openreview_page = (EVIDENCE / "response_2").read_text(encoding="utf-8")
    required = {
        "ACS snapshot/version and exact extraction": True,
        "paper-era preprocessing, split, XGBoost parameters, and seeds": True,
        "active/classical/uniform runner and 3000-trial outputs": True,
    }
    return {
        "audit_type": "authoritative_material_and_primary_provenance_availability_only",
        "retrieval_statuses": records.splitlines(),
        "github_exact_title_repository_count": title_search["total_count"],
        "github_aipw_u_statistic_repository_count": aipw_search["total_count"],
        "arxiv_page_has_direct_github_link": "github.com" in arxiv_page.lower(),
        "openreview_page_has_direct_github_link": "github.com" in openreview_page.lower(),
        "openreview_api_accessible_without_auth": records.splitlines()[0].startswith("200\t"),
        "source_comparison": {
            "figure_compares_classical_and_uniform": "{classical} and {uniform} baselines" in source,
            "60_percent_is_explicitly_relative_to_classical": "60\\% labeling-budget reduction relative to {classical}" in source,
            "near_nominal_coverage_reported": "All methods achieve near-nominal coverage" in source,
        },
        "required_source_faithful_artifacts_still_unavailable": required,
        "source_faithful_cpu_run_executed": False,
        "verdict": "inconclusive_source_artifact_scope",
        "reason": (
            "The retained arXiv/OpenReview records and public GitHub repository "
            "searches provide no author executable or supplementary experimental "
            "artifact. The source explicitly attributes its roughly 60% saving to "
            "the classical baseline, not uniform. Without the ACS version/extraction, "
            "paper-era split/hyperparameters/seeds, and trial outputs, a CPU ACS run "
            "would be a proxy and cannot resolve the live uniform-comparison claim."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(calculate(), indent=2, sort_keys=True))
