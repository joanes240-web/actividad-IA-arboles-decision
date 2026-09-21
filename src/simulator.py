from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
import json
import math


@dataclass(frozen=True)
class ModelParams:
    version_modelo: str
    T0_horas: float
    Gmax: float
    beta_c: float
    beta_r: float
    beta_p: float

    def validate(self) -> None:
        if self.T0_horas <= 0:
            raise ValueError("T0_horas debe ser > 0")
        if not (0 < self.Gmax < 1):
            raise ValueError("Gmax debe estar entre 0 y 1")
        if min(self.beta_c, self.beta_r, self.beta_p) < 0:
            raise ValueError("Los coeficientes beta deben ser no negativos")


def load_params(path: str | Path) -> ModelParams:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    params = ModelParams(
        version_modelo=str(data["version_modelo"]),
        T0_horas=float(data["T0_horas"]),
        Gmax=float(data["Gmax"]),
        beta_c=float(data["beta_c"]),
        beta_r=float(data["beta_r"]),
        beta_p=float(data["beta_p"]),
    )
    params.validate()
    return params


def _validate_input(name: str, value: float) -> float:
    value = float(value)
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} debe estar en [0, 1]")
    return value


def simulate(c: float, r: float, p: float, params: ModelParams, beta_factor: float = 1.0) -> dict:
    """Calcula G, T_s y E_s para un escenario determinístico.

    beta_factor se utiliza únicamente para sensibilidad local de coeficientes.
    """
    c = _validate_input("c", c)
    r = _validate_input("r", r)
    p = _validate_input("p", p)
    beta_factor = float(beta_factor)
    if beta_factor < 0:
        raise ValueError("beta_factor debe ser >= 0")

    x = beta_factor * (params.beta_c * c + params.beta_r * r + params.beta_p * p)
    G = params.Gmax * (1.0 - math.exp(-x))
    T_s = params.T0_horas * (1.0 - G)
    E_s = params.T0_horas / T_s

    return {
        "version_modelo": params.version_modelo,
        "c": c,
        "r": r,
        "p": p,
        "beta_factor": beta_factor,
        "G": G,
        "reduccion_pct": G * 100.0,
        "T_s_horas": T_s,
        "E_s": E_s,
    }


def run_scenarios(scenarios: Iterable[dict], params: ModelParams) -> list[dict]:
    out = []
    for scenario in scenarios:
        result = simulate(scenario["c"], scenario["r"], scenario["p"], params)
        result["escenario"] = scenario["name"]
        out.append(result)
    return out
