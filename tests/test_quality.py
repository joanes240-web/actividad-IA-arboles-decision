import pandas as pd

from src.quality import validate_completeness, validate_unique, validate_temporal_order


def test_completeness():
    s = pd.Series([1, 2, None, 4])
    result = validate_completeness(s, 0.75)
    assert result["passed"] is True
    assert result["value"] == 0.75


def test_uniqueness():
    df = pd.DataFrame({"ticket_id": [1, 2, 3]})
    assert validate_unique(df, ["ticket_id"])["passed"] is True


def test_temporal_consistency():
    learning = pd.Series(["2026-01-01", "2026-03-01"])
    operation = pd.Series(["2026-02-01", "2026-02-15"])
    result = validate_temporal_order(learning, operation)
    assert result["invalid_rows"] == 1
    assert result["passed"] is False
