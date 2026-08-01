from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from claim1_aipw_enumeration import run


def test_aipw_matches_conditional_u_statistic_and_theta_star():
    result = run()
    assert result["enumeration_cells"] == 64
    assert result["AIPW_abs_error_vs_theta_star"] < 1e-12
    assert result["max_conditional_AIPW_abs_error_vs_U_y"] < 1e-12


def test_omitting_inverse_probability_weights_is_biased():
    result = run()
    assert result["bad_unweighted_abs_bias_vs_theta_star"] > 1e-3
