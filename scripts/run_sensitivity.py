from pathlib import Path
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.simulator import load_params, simulate


def main() -> None:
    params = load_params(ROOT / "config" / "model_params.json")
    rows = []
    for factor in (0.9, 1.0, 1.1):
        result = simulate(1, 1, 1, params, beta_factor=factor)
        rows.append({
            "factor_beta": factor,
            "factor_pct": int(round(factor * 100)),
            "G": result["G"],
            "reduccion_pct": result["reduccion_pct"],
            "T_s_horas": result["T_s_horas"],
            "E_s": result["E_s"],
            "version_modelo": result["version_modelo"],
        })

    df = pd.DataFrame(rows)
    out = ROOT / "results" / "sensitivity_aggregated.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(df.to_string(index=False))
    print(f"\nResultado guardado en: {out}")


if __name__ == "__main__":
    main()
