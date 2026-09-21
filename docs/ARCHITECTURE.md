# Arquitectura analítica

## Capas

### 1. Fuentes
Sistemas de personas, aprendizaje, certificaciones, soporte, KPIs e interacción temporal.

### 2. Preparación
Perfilamiento, tipificación, fechas, catálogos, deduplicación documentada y validación de granularidad.

### 3. Privacidad
Separación de identificadores directos, pseudonimización y minimización antes de cruces transversales.

### 4. Capa analítica
Dimensiones conformadas, hechos, caso base, parámetros y `FactEscenario`.

### 5. Decisión
KPIs, escenarios, sensibilidad y visualizaciones etiquetadas explícitamente como simulación.

## Gobierno transversal

Cada salida relevante debe permitir reconstruir:

1. fuente;
2. transformación;
3. regla de calidad;
4. versión de código/modelo;
5. supuestos y parámetros.

## Escalabilidad

- **Nivel 1:** notebook mononodo para EDA y validación.
- **Nivel 2:** pipeline programado con Parquet/PostgreSQL y métricas persistentes.
- **Nivel 3:** Spark/Databricks cuando la memoria, uniones, ventana histórica, concurrencia o frecuencia lo exijan.

El criterio es proporcionalidad tecnológica: no sobredimensionar el piloto, pero conservar contratos que permitan migrar sin cambiar la semántica.
