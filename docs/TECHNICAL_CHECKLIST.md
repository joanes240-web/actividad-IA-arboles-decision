# Checklist técnico previo a ejecución/publicación

- [ ] Verificar versión del dataset y fecha de corte.
- [ ] Verificar que la PII fue retirada antes de la capa integrada.
- [ ] Validar nulos de las variables requeridas por cada KPI.
- [ ] Validar cardinalidad y granularidad de llaves.
- [ ] Revisar conteos antes y después de cada join.
- [ ] Recalcular T0 para la población y ventana seleccionadas cuando corresponda.
- [ ] Registrar versión de Gmax y coeficientes beta.
- [ ] Ejecutar pruebas de reproducción, monotonicidad y límites.
- [ ] Ejecutar sensibilidad de parámetros.
- [ ] Etiquetar toda salida como observada o simulada.
- [ ] Registrar versión/hash de código y fecha de ejecución.
- [ ] Sanitizar notebook y revisar manualmente su contenido.
- [ ] Confirmar que no se incluyen muestras reales, PII, credenciales o secretos.
- [ ] Confirmar que los resultados públicos son agregados o sintéticos.
