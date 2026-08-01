from src.claim2_optimal_sampling import BUDGET, calculate


def test_projection_score_rule_is_budget_feasible_and_beats_controls():
    result = calculate()
    assert abs(sum(result["optimal_pi_sqrt_s"]) - BUDGET) < 1e-12
    assert all(0 < probability < 1 for probability in result["optimal_pi_sqrt_s"])
    assert not result["clipping_active"]
    assert result["leading_objective_optimal"] < result["leading_objective_raw_residual_control"]
    assert result["leading_objective_optimal"] < result["leading_objective_uniform"]


def test_independent_grid_agrees_with_closed_form_neighborhood():
    result = calculate()
    # The brute-force 0.01 grid cannot beat the analytic constrained solution.
    assert result["leading_objective_optimal"] <= result["finite_grid_best"]["objective"] + 1e-12
    for exact, grid in zip(result["optimal_pi_sqrt_s"], result["finite_grid_best"]["pi"]):
        assert abs(exact - grid) <= 0.02
