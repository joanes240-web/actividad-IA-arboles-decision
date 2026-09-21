# Política de publicación y confidencialidad

## Permitido en el repositorio público

- código fuente;
- notebook sanitizado sin outputs sensibles;
- parámetros versionados;
- pruebas automatizadas;
- documentación metodológica;
- resultados agregados del simulador;
- datos 100% sintéticos claramente etiquetados.

## No permitido

- datasets empresariales originales;
- muestras de registros reales, incluso si son pequeñas;
- archivos exportados desde el notebook que contengan registros;
- nombre, correo, documento u otros identificadores directos;
- credenciales, secretos, tokens o salts de pseudonimización;
- `Resumen_EDA_Proyecto.xlsx` y artefactos internos equivalentes;
- resultados de grupos tan pequeños que permitan reidentificación indirecta.

## Pseudonimización

Una llave pseudonimizada no convierte automáticamente un dataset real en anónimo. Si existe posibilidad razonable de reidentificación, el dataset debe mantenerse en el entorno controlado.

## Outputs del notebook

La versión pública debe eliminar outputs de ejecución y ser revisada manualmente antes del commit.

## Autoría académica

La versión depositada debe ser entendida, revisada, ejecutada y defendida por el autor del TFM. Los commits académicos deben mantenerse bajo su autoría.
