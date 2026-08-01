from src.claim4_falsification_comparator_audit import calculate


def test_live_uniform_comparator_is_not_the_paper_60_percent_comparator():
    result = calculate()
    facts = result["source_facts"]
    assert facts["exact_60_percent_relative_to_classical"]
    assert not facts["exact_60_percent_relative_to_uniform"]
    assert facts["classical_is_ipw_under_uniform_sampling"]
    assert facts["uniform_is_aipw_under_uniform_sampling"]
    assert facts["methods_are_distinct_despite_same_sampling_policy"]
    assert result["verdict"] == "falsified_literal_comparator_attribution"
    assert not result["source_faithful_acs_rerun_executed"]
