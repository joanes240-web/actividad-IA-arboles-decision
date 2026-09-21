from __future__ import annotations

import pandas as pd


def profile_dataframe(df: pd.DataFrame, source_name: str = "dataset") -> dict:
    memory_mb = float(df.memory_usage(deep=True).sum() / (1024 ** 2))
    null_pct = (df.isna().mean() * 100).round(4).to_dict()
    return {
        "source": source_name,
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "memory_mb": round(memory_mb, 4),
        "duplicate_full_rows": int(df.duplicated().sum()),
        "dtypes": {c: str(t) for c, t in df.dtypes.items()},
        "null_pct": null_pct,
    }


def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    cols = df.select_dtypes(include="number").columns
    if len(cols) == 0:
        return pd.DataFrame()
    return df[cols].describe().T


def categorical_summary(df: pd.DataFrame, top_n: int = 10) -> dict[str, list[tuple]]:
    result = {}
    for col in df.select_dtypes(include=["object", "category", "string"]).columns:
        counts = df[col].value_counts(dropna=False).head(top_n)
        result[col] = [(str(k), int(v)) for k, v in counts.items()]
    return result


def common_columns(datasets: dict[str, pd.DataFrame]) -> list[dict]:
    names = list(datasets)
    out = []
    for i, left in enumerate(names):
        for right in names[i+1:]:
            common = sorted(set(datasets[left].columns) & set(datasets[right].columns))
            if common:
                out.append({"left": left, "right": right, "common_columns": common})
    return out
