from src.claim4_attempt3_acs_provenance_audit import calculate


def test_primary_acs_archive_audit_is_inconclusive_not_proxy_verification():
    result = calculate()
    records = result["census_primary_records"]
    paper = result["paper_acs_section"]
    assert records["microdata_page_http_status"] == "200"
    assert records["pums_2023_1_year_directory_http_status"] == "200"
    assert records["pums_2022_1_year_directory_http_status"] == "200"
    assert records["distinct_2022_2023_archive_listing_hashes"]
    assert paper["explicitly_names_60_percent_comparator"]
    assert not paper["explicitly_names_uniform_60_percent_comparator"]
    assert len(paper["required_protocol_fields_not_specified"]) == 6
    assert result["verdict"] == "inconclusive_source_artifact_scope"
    assert not result["source_faithful_cpu_run_executed"]
