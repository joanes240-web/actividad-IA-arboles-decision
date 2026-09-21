# TFM · Simulación del impacto del aprendizaje en la productividad

Repositorio técnico reproducible del Trabajo Fin de Máster **“Simulación del impacto del aprendizaje en la productividad en entornos de consultoría basados en datos operativos”**.

## Objetivo

El proyecto implementa una arquitectura analítica para integrar aprendizaje y productividad y reproduce un simulador determinístico **what-if**. El repositorio público está diseñado para ser auditable sin publicar datasets empresariales, credenciales, PII ni muestras de registros reales.

## Alcance técnico

La solución se organiza en cinco capas:

1. **Fuentes**: sistemas operativos y de aprendizaje.
2. **Preparación**: perfilamiento, tipificación, limpieza y deduplicación controlada.
3. **Privacidad**: separación de PII, pseudonimización y minimización.
4. **Capa analítica**: dimensiones, hechos, caso base y escenarios.
5. **Decisión**: KPIs, sensibilidad, visualización y priorización.

El gobierno del dato es transversal: calidad, diccionario, linaje, versiones, acceso y trazabilidad.

## Modelo what-if

Entradas normalizadas:

- `c`: intensidad / cobertura, en [0, 1].
- `r`: recencia, en [0, 1].
- `p`: pertinencia, en [0, 1].

Ecuaciones:

```text
G(c,r,p) = Gmax * [1 - exp(-(beta_c*c + beta_r*r + beta_p*p))]
T_s      = T0 * (1 - G)
E_s      = T0 / T_s
```

Parámetros de la versión académica:

| Parámetro | Valor |
|---|---:|
| T0 | 42.0 h |
| Gmax | 0.2678077 |
| beta_c | 0.5288919 |
| beta_r | 0.7796493 |
| beta_p | 1.0705728 |

> **Importante:** los coeficientes fueron calibrados para reproducir los escenarios del piloto. No son efectos causales ni estimaciones estadísticas.

## Escenarios reproducibles

| Escenario | c | r | p | Reducción | T_s (h) | E_s |
|---|---:|---:|---:|---:|---:|---:|
| Caso base | 0 | 0 | 0 | 0.0% | 42.0 | 1.000 |
| Capacitación intensiva | 1 | 0 | 0 | 11.0% | 37.4 | 1.124 |
| Actualización recurrente | 0 | 1 | 0 | 14.5% | 35.9 | 1.170 |
| Certificación priorizada | 0 | 0 | 1 | 17.6% | 34.6 | 1.214 |
| Escenario combinado | 1 | 1 | 1 | 24.3% | 31.8 | 1.321 |

## Estructura

```text
.
├── config/
│   ├── model_params.json
│   ├── scenarios.json
│   └── quality_rules.json
├── data/
│   ├── README.md
│   └── synthetic/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DATA_DICTIONARY.md
│   ├── METHODOLOGY.md
│   ├── MODEL_CARD.md
│   ├── PUBLICATION_POLICY.md
│   └── TECHNICAL_CHECKLIST.md
├── notebooks/
│   └── README.md
├── results/
│   ├── scenarios_aggregated.csv
│   ├── sensitivity_aggregated.csv
│   └── README.md
├── scripts/
│   ├── generate_synthetic_demo.py
│   ├── run_sensitivity.py
│   ├── run_simulation.py
│   └── sanitize_notebook.py
├── src/
│   ├── dimensional_contracts.py
│   ├── lineage.py
│   ├── privacy.py
│   ├── profiling.py
│   ├── quality.py
│   └── simulator.py
├── tests/
│   ├── test_privacy.py
│   ├── test_quality.py
│   └── test_simulator.py
├── .github/workflows/tests.yml
├── .gitignore
└── requirements.txt
```

## Instalación en Windows / PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecución

Reproducir escenarios:

```powershell
python scripts/run_simulation.py
```

Ejecutar sensibilidad ±10%:

```powershell
python scripts/run_sensitivity.py
```

Generar un dataset sintético demostrativo:

```powershell
python scripts/generate_synthetic_demo.py
```

Ejecutar pruebas:

```powershell
pytest -q
```

Sanitizar el notebook de EDA antes de publicarlo:

```powershell
python scripts/sanitize_notebook.py "Gestion Bases de Datos/EDA_Completo_Proyecto.ipynb" "notebooks/EDA_Completo_Proyecto.ipynb"
```

El sanitizador elimina outputs y contadores de ejecución. Aun así, el autor debe revisar manualmente markdown, código, rutas y metadatos antes de publicar.

## Reproducibilidad

La reproducibilidad se divide en dos niveles:

- **Matemática:** completa. Los parámetros, ecuaciones y pruebas permiten reproducir los escenarios publicados.
- **Datos:** restringida. Los datos fuente son confidenciales y no forman parte del repositorio. La estructura puede demostrarse con datos sintéticos.

## Política de datos

No publicar:

- datasets empresariales originales;
- exportaciones con registros o muestras reales;
- nombres, correos, documentos u otros identificadores directos;
- credenciales, tokens, secretos o rutas con información sensible;
- `Resumen_EDA_Proyecto.xlsx` ni artefactos internos equivalentes.

Consulte `docs/PUBLICATION_POLICY.md` y `data/README.md`.

## Interpretación

El simulador sirve para comparar escenarios bajo supuestos explícitos. **No demuestra causalidad** y no debe utilizarse para rankings individuales de personas ni decisiones sancionatorias.
