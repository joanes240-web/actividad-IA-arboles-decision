"""Contratos conceptuales del modelo dimensional descrito en el TFM."""

DIMENSIONAL_MODEL = {
    "DimPersona": {
        "grain": "Una fila por persona pseudonimizada y vigencia",
        "keys_attributes": ["id_persona_hash", "unidad", "rol", "nivel"],
        "use": "Segmentación sin PII",
    },
    "DimTiempo": {
        "grain": "Una fila por fecha/periodo",
        "keys_attributes": ["fecha", "semana", "mes", "trimestre"],
        "use": "Ventanas antes/después",
    },
    "DimCurso": {
        "grain": "Una fila por curso",
        "keys_attributes": ["curso_id", "tipo", "duracion", "modalidad"],
        "use": "Intensidad y cobertura",
    },
    "DimHabilidad": {
        "grain": "Una fila por habilidad/categoría",
        "keys_attributes": ["habilidad", "dominio", "demanda"],
        "use": "Pertinencia",
    },
    "DimUnidad": {
        "grain": "Una fila por unidad/proceso",
        "keys_attributes": ["unidad", "cliente", "proceso"],
        "use": "Comparación organizacional",
    },
    "FactTickets": {
        "grain": "Un evento/ticket",
        "keys_attributes": ["persona_hash", "fecha", "categoria"],
        "metrics": ["tiempo_resolucion_horas", "volumen"],
    },
    "FactAprendizaje": {
        "grain": "Una actividad formativa",
        "keys_attributes": ["persona_hash", "curso", "fecha"],
        "metrics": ["asistencia", "finalizacion", "horas"],
    },
    "FactCertificacion": {
        "grain": "Una certificación/evento",
        "keys_attributes": ["persona_hash", "habilidad", "fecha"],
        "metrics": ["estado", "vigencia"],
    },
    "FactKPI": {
        "grain": "Unidad-periodo-indicador",
        "keys_attributes": ["unidad", "periodo", "indicador"],
        "metrics": ["valor_kpi"],
    },
    "FactEscenario": {
        "grain": "Escenario-versión-segmento",
        "keys_attributes": ["escenario", "parametros", "version"],
        "metrics": ["T_s", "G_s", "E_s"],
    },
}
