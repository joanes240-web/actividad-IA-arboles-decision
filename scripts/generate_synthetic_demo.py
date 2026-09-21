from pathlib import Path
import hashlib
import random
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "synthetic" / "synthetic_demo.csv"


def fake_hash(i: int) -> str:
    return hashlib.sha256(f"SYNTHETIC_PERSON_{i}".encode("utf-8")).hexdigest()


def main(seed: int = 42, n: int = 120) -> None:
    rng = random.Random(seed)
    units = ["Unidad_A", "Unidad_B", "Unidad_C"]
    skills = ["Analitica", "Soporte", "Procesos", "Datos"]
    certs = ["vigente", "vencida", "no_aplica"]

    rows = []
    for i in range(n):
        person = rng.randint(1, 35)
        c = round(rng.random(), 3)
        r = round(rng.random(), 3)
        p = round(rng.random(), 3)
        rows.append({
            "id_persona_hash": fake_hash(person),
            "fecha": pd.Timestamp("2026-01-01") + pd.Timedelta(days=rng.randint(0, 240)),
            "unidad_negocio": rng.choice(units),
            "curso_id": f"CURSO_{rng.randint(1, 12):02d}",
            "habilidad": rng.choice(skills),
            "estado_certificacion": rng.choice(certs),
            "ticket_id": f"TKT_SYN_{i+1:05d}",
            "tiempo_resolucion_horas": round(max(1.0, rng.gauss(42, 14)), 2),
            "c": c,
            "r": r,
            "p": p,
            "version_modelo": "1.0.0",
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUT, index=False, encoding="utf-8")
    print(f"Dataset 100% sintético generado en {OUT}")
    print("No replica registros reales ni pretende reproducir distribuciones empresariales exactas.")


if __name__ == "__main__":
    main()
