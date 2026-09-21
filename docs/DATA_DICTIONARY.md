# Diccionario de variables analíticas

| Variable | Descripción | Uso |
|---|---|---|
| `id_persona_hash` | Llave técnica pseudonimizada | Dimensión persona e integración sin PII directa |
| `fecha` | Fecha de evento o indicador | Dimensión tiempo y ventanas |
| `unidad_negocio` | Unidad, proceso o canal operativo | Segmentación |
| `curso_id` | Identificador del curso | Dimensión curso |
| `habilidad` | Competencia relacionada | Dimensión habilidad y pertinencia |
| `estado_certificacion` | Resultado/vigencia de certificación | Hecho certificación |
| `ticket_id` | Identificador técnico del ticket | Hecho tickets |
| `tiempo_resolucion_horas` | Duración válida del ticket | KPI operativo y caso base |
| `c` | Intensidad/cobertura normalizada | Entrada del simulador |
| `r` | Recencia normalizada | Entrada del simulador |
| `p` | Pertinencia normalizada | Entrada del simulador |
| `G` | Reducción relativa simulada | Salida intermedia |
| `T_s` | Tiempo medio simulado | KPI de escenario |
| `E_s` | `T0/Ts` | Índice de eficiencia relativo |
| `version_modelo` | Versión de parámetros y lógica | Trazabilidad y auditoría |

## Granularidad conceptual

Los contratos de dimensiones y hechos se encuentran en `src/dimensional_contracts.py`. Las tablas transaccionales no deben unirse entre sí sin declarar previamente granularidad, cardinalidad y ventana temporal.
