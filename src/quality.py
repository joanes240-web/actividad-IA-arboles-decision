from __future__ import annotations

from typing import Iterable
import pandas as pd


def completeness_ratio(series: pd.Series) -> float:
    """Proporción de valores no nulos entre 0 y 1."""
    if len(series) == 0:
        return 0.0
    return float(series.notna().mean())


def validate_completeness(series: pd.Series, threshold: float) -> dict:
    if not 0 <= threshold <= 1:
        raise ValueError("threshold debe estar en [0, 1]")
    ratio = completeness_ratio(series)
    return {"metric": "completitud", "value": ratio, "threshold": threshold, "passed": ratio >= threshold}


def validate_unique(df: pd.DataFrame, keys: Iterable[str]) -> dict:
    keys = list(keys)
    missing = [k for k in keys if k not in df.columns]
    if missing:
        raise KeyError(f"Columnas no encontradas: {missing}")
    duplicate_rows = int(df.duplicated(subset=keys, keep=False).sum())
    return {"metric": "unicidad", "keys": keys, "duplicate_rows": duplicate_rows, "passed": duplicate_rows == 0}


def validate_range(series: pd.Series, min_value: float | None = None, max_value: float | None = None) -> dict:
    valid = series.dropna()
    mask = pd.Series(True, index=valid.index)
    if min_value is not None:
        mask &= valid >= min_value
    if max_value is not None:
        mask &= valid <= max_value
    invalid_count = int((~mask).sum())
    return {"metric": "validez_rango", "invalid_count": invalid_count, "passed": invalid_count == 0}


def validate_temporal_order(learning_date: pd.Series, operational_date: pd.Series) -> dict:
    learning = pd.to_datetime(learning_date, errors="coerce")
    operational = pd.to_datetime(operational_date, errors="coerce")
    comparable = learning.notna() & operational.notna()
    invalid = comparable & (learning > operational)
    return {
        "metric": "consistencia_temporal",
        "comparable_rows": int(comparable.sum()),
        "invalid_rows": int(invalid.sum()),
        "passed": int(invalid.sum()) == 0,
    }


def validate_join_row_growth(before_left: int, before_right: int, after_join: int, expected: str = "many_to_one") -> dict:
    """Control simple para detectar multiplicación inesperada después de un join.

    Para many_to_one, el resultado no debería superar el número de filas del lado izquierdo.
    Para one_to_one, tampoco debería superar el mayor de los dos lados.
    """
    if expected == "many_to_one":
        limit = before_left
    elif expected == "one_to_one":
        limit = max(before_left, before_right)
    else:
        raise ValueError("expected soporta 'many_to_one' u 'one_to_one'")
    return {"metric": "crecimiento_join", "after_join": after_join, "limit": limit, "passed": after_join <= limit}
