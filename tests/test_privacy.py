import pandas as pd

from src.privacy import detect_direct_identifier_columns, drop_direct_identifiers, pseudonymize_identifier


def test_detect_and_drop_direct_identifiers():
    df = pd.DataFrame({"Nombre": ["Persona Demo"], "Correo": ["demo@example.invalid"], "unidad": ["A"]})
    detected = detect_direct_identifier_columns(df.columns)
    assert "Nombre" in detected
    assert "Correo" in detected
    clean, removed = drop_direct_identifiers(df)
    assert set(removed) == {"Nombre", "Correo"}
    assert list(clean.columns) == ["unidad"]


def test_pseudonymization_is_deterministic_for_same_salt():
    s = pd.Series(["ID_DEMO_1", "ID_DEMO_1"])
    out = pseudonymize_identifier(s, salt="SALT_SOLO_PARA_TEST")
    assert out.iloc[0] == out.iloc[1]
    assert len(out.iloc[0]) == 64
