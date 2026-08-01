from src.claim3_crn_coupling import calculate


def test_h2_coupled_difference_shrinks() -> None:
    result = calculate()
    rows = result["h2_satisfying_crn_results"]
    assert result["adaptive_rms_decreases"]
    assert rows[-1]["delta_sup"] < rows[0]["delta_sup"]
    assert rows[-1]["rms_sqrt_n_difference"] < rows[0]["rms_sqrt_n_difference"]


def test_fixed_policy_error_negative_control_remains_visible() -> None:
    result = calculate()
    assert result["control_rms_not_small_at_largest_n"]
    # At the largest n, the H2-respecting policy is materially closer under
    # the same-uniform coupling than a policy with fixed misspecification.
    assert (
        result["h2_satisfying_crn_results"][-1]["rms_sqrt_n_difference"]
        < result["fixed_error_h2_violation_negative_control"][-1]["rms_sqrt_n_difference"]
    )
