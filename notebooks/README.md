# Notebooks públicos

Las versiones públicas de los notebooks deben conservar el código reproducible, pero no outputs con registros, PII, rutas sensibles ni muestras empresariales. El notebook principal es `EDA_Completo_Proyecto.ipynb`; cualquier notebook auxiliar debe pasar por el mismo proceso de sanitización.

Para crear una copia sin outputs:

```powershell
python scripts/sanitize_notebook.py "Gestion Bases de Datos/EDA_Completo_Proyecto.ipynb" "notebooks/EDA_Completo_Proyecto.ipynb"
```

Después del proceso automático realice una **revisión manual** de:

- celdas Markdown;
- rutas de archivos;
- nombres de organización o cliente;
- credenciales o tokens;
- celdas con listas/prints que hayan quedado escritas en el código;
- metadatos del notebook.
