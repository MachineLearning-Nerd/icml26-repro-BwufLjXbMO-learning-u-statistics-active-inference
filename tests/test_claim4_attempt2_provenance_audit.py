from src.claim4_attempt2_provenance_audit import calculate


def test_authoritative_search_retains_no_executable_protocol() -> None:
    result = calculate()
    assert result["github_exact_title_repository_count"] == 0
    assert result["github_aipw_u_statistic_repository_count"] == 0
    assert result["source_faithful_cpu_run_executed"] is False
    assert result["verdict"] == "inconclusive_source_artifact_scope"
    assert all(result["required_source_faithful_artifacts_still_unavailable"].values())


def test_live_uniform_comparison_is_not_supported_by_60_percent_sentence() -> None:
    result = calculate()
    comparison = result["source_comparison"]
    assert comparison["figure_compares_classical_and_uniform"] is True
    assert comparison["60_percent_is_explicitly_relative_to_classical"] is True
    assert comparison["near_nominal_coverage_reported"] is True
