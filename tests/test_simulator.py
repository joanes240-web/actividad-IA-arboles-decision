from pathlib import Path
import pytest

from src.simulator import load_params, simulate

ROOT = Path(__file__).resolve().parents[1]
PARAMS = load_params(ROOT / "config" / "model_params.json")


def test_base_case():
    x = simulate(0, 0, 0, PARAMS)
    assert x["G"] == pytest.approx(0.0, abs=1e-12)
    assert x["T_s_horas"] == pytest.approx(42.0, abs=1e-12)
    assert x["E_s"] == pytest.approx(1.0, abs=1e-12)


@pytest.mark.parametrize(
    "c,r,p,expected_g,expected_t,expected_e",
    [
        (1, 0, 0, 0.110, 37.38, 1.124),
        (0, 1, 0, 0.145, 35.91, 1.170),
        (0, 0, 1, 0.176, 34.608, 1.214),
        (1, 1, 1, 0.243, 31.794, 1.321),
    ],
)
def test_published_scenarios(c, r, p, expected_g, expected_t, expected_e):
    x = simulate(c, r, p, PARAMS)
    assert x["G"] == pytest.approx(expected_g, abs=2e-6)
    assert x["T_s_horas"] == pytest.approx(expected_t, abs=0.002)
    assert x["E_s"] == pytest.approx(expected_e, abs=0.001)


def test_bounds_and_positive_time():
    for c, r, p in [(0,0,0), (0.25,0.5,0.75), (1,1,1)]:
        x = simulate(c, r, p, PARAMS)
        assert 0 <= x["G"] <= PARAMS.Gmax
        assert x["T_s_horas"] > 0


def test_monotonicity_each_dimension():
    base = simulate(0.2, 0.2, 0.2, PARAMS)["T_s_horas"]
    assert simulate(0.3, 0.2, 0.2, PARAMS)["T_s_horas"] <= base
    assert simulate(0.2, 0.3, 0.2, PARAMS)["T_s_horas"] <= base
    assert simulate(0.2, 0.2, 0.3, PARAMS)["T_s_horas"] <= base


def test_combined_sensitivity():
    low = simulate(1,1,1,PARAMS,beta_factor=0.9)
    mid = simulate(1,1,1,PARAMS,beta_factor=1.0)
    high = simulate(1,1,1,PARAMS,beta_factor=1.1)
    assert low["reduccion_pct"] == pytest.approx(23.63, abs=0.02)
    assert mid["reduccion_pct"] == pytest.approx(24.30, abs=0.02)
    assert high["reduccion_pct"] == pytest.approx(24.83, abs=0.02)
    assert low["T_s_horas"] == pytest.approx(32.07, abs=0.02)
    assert high["T_s_horas"] == pytest.approx(31.57, abs=0.02)


def test_inputs_must_be_normalized():
    with pytest.raises(ValueError):
        simulate(1.1, 0, 0, PARAMS)
