from src.claim5_falsification_source_scope_audit import calculate


def test_live_claim_5_has_exact_primary_source_support_not_a_literal_contradiction():
    result = calculate()
    facts = result["source_facts"]
    assert facts["vitaldb_heading_present"]
    assert facts["hemoglobin_pairing_protocol_present"]
    assert facts["wilcoxon_target_present"]
    assert facts["exact_20_percent_classical_statement_present"]
    assert not facts["contradictory_20_percent_uniform_statement_present"]
    assert facts["near_nominal_coverage_statement_present"]
    assert result["verdict"] == "inconclusive_literal_source_supports_claim"
    assert not result["source_faithful_vitaldb_rerun_executed"]
