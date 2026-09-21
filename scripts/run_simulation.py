from pathlib import Path
import json
import sys
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.simulator import load_params, run_scenarios


def main() -> None:
    params = load_params(ROOT / "config" / "model_params.json")
    scenario_cfg = json.loads((ROOT / "config" / "scenarios.json").read_text(encoding="utf-8"))
    results = run_scenarios(scenario_cfg["scenarios"], params)

    df = pd.DataFrame(results)[
        ["escenario", "c", "r", "p", "G", "reduccion_pct", "T_s_horas", "E_s", "version_modelo"]
    ]
    out = ROOT / "results" / "scenarios_aggregated.csv"
    df.to_csv(out, index=False, encoding="utf-8")
    print(df.to_string(index=False))
    print(f"\nResultado guardado en: {out}")


if __name__ == "__main__":
    main()
