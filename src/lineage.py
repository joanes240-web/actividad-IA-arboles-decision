from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json


def build_lineage_record(*, source: str, rule: str, target_field: str | None = None,
                         data_version: str | None = None, model_version: str | None = None,
                         validator: str | None = None) -> dict:
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source": source,
        "data_version": data_version,
        "rule": rule,
        "target_field": target_field,
        "model_version": model_version,
        "validator": validator,
    }


def append_lineage_jsonl(record: dict, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
