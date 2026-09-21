from __future__ import annotations

import hashlib
import re
from typing import Iterable
import pandas as pd

DIRECT_IDENTIFIER_PATTERNS = (
    r"^nombre$",
    r"nombre[_ ]?completo",
    r"correo|email|e[-_ ]?mail",
    r"documento|cedula|c[eé]dula|dni|passport|pasaporte",
    r"telefono|tel[eé]fono|celular|mobile",
)


def _normalize(name: str) -> str:
    return re.sub(r"\s+", " ", str(name).strip().lower())


def detect_direct_identifier_columns(columns: Iterable[str]) -> list[str]:
    detected = []
    for col in columns:
        n = _normalize(col)
        if any(re.search(pattern, n, flags=re.IGNORECASE) for pattern in DIRECT_IDENTIFIER_PATTERNS):
            detected.append(col)
    return detected


def drop_direct_identifiers(df: pd.DataFrame, extra_columns: Iterable[str] = ()) -> tuple[pd.DataFrame, list[str]]:
    detected = set(detect_direct_identifier_columns(df.columns)) | set(extra_columns)
    present = [c for c in df.columns if c in detected]
    return df.drop(columns=present).copy(), present


def pseudonymize_identifier(series: pd.Series, salt: str) -> pd.Series:
    """Genera una llave técnica SHA-256.

    Pseudonimización no equivale a anonimización. El salt debe permanecer fuera del repositorio.
    """
    if not salt:
        raise ValueError("Se requiere un salt no vacío y fuera del repositorio")

    def digest(value):
        if pd.isna(value):
            return pd.NA
        raw = f"{salt}|{value}".encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    return series.map(digest)
