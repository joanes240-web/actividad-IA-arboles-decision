# Metodología técnica

El piloto adapta CRISP-DM a seis fases:

1. Comprensión del negocio.
2. Comprensión de datos.
3. Preparación.
4. Modelado.
5. Evaluación.
6. Despliegue analítico.

La privacidad y el gobierno son transversales.

## Flujo reproducible

1. Definir rutas, configuración y versión del modelo.
2. Cargar CSV/Excel con selección de columnas y tipos.
3. Perfilar dimensiones, tipos, nulos, duplicados y rangos temporales.
4. Remover o pseudonimizar PII antes de integrar.
5. Estandarizar fechas, catálogos, llaves y granularidad.
6. Validar relaciones candidatas y construir dimensiones/hechos mínimos.
7. Calcular T0 y métricas complementarias.
8. Cargar Gmax y coeficientes beta desde configuración versionada.
9. Generar escenarios y calcular G, T_s y E_s.
10. Ejecutar sensibilidad y pruebas de monotonicidad/límites.
11. Exportar únicamente resultados agregados y bitácora de supuestos.
12. Registrar versión de código, datos, reglas y parámetros.

## Reglas de calidad

- **Completitud:** se define por campo crítico y KPI, no por promedio global.
- **Unicidad:** una repetición puede ser válida en tablas de eventos; la granularidad manda.
- **Validez:** tipos, rangos y catálogos deben ser compatibles con la definición.
- **Consistencia temporal:** aprendizaje no puede atribuirse a desempeño anterior.
- **Trazabilidad:** un KPI sin linaje reconstruible no debe publicarse.

## Separación EDA / simulador

El EDA caracteriza datos. El simulador funciona con parámetros publicados y no necesita cargar datos personales para reproducir los escenarios académicos.
