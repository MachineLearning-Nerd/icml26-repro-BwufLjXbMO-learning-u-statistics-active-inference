from src.claim4_acs_availability_audit import calculate


def test_source_names_claim4_protocol_facts() -> None:
    result = calculate()
    facts = result["source_facts"]
    assert all(facts.values())
    assert "Figure/combined_gini.pdf" in result["retained_source_files"]


def test_missing_release_inputs_prevent_full_claim_label() -> None:
    result = calculate()
    assert result["source_faithful_cpu_run_executed"] is False
    assert result["verdict"] == "inconclusive_source_artifact_scope"
    assert all(result["required_inputs_absent_from_retained_release"].values())
