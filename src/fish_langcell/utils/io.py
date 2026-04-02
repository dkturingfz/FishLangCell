"""I/O helpers for Fish-LangCell scaffolding."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any



def load_yaml(path: str | Path) -> dict[str, Any]:
    """Load a YAML file into a dictionary."""
    path_obj = Path(path)
    if not path_obj.exists():
        raise FileNotFoundError(f"YAML config not found: {path_obj}")
    with path_obj.open("r", encoding="utf-8") as handle:
        import yaml

        data = yaml.safe_load(handle)
    return data or {}


def load_tsv_rows(path: str | Path) -> list[dict[str, str]]:
    """Load TSV rows as a list of dictionaries."""
    path_obj = Path(path)
    if not path_obj.exists():
        raise FileNotFoundError(f"TSV file not found: {path_obj}")
    with path_obj.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return list(reader)


def load_tsv_header(path: str | Path) -> list[str]:
    """Load only TSV header columns."""
    path_obj = Path(path)
    if not path_obj.exists():
        raise FileNotFoundError(f"TSV file not found: {path_obj}")
    with path_obj.open("r", encoding="utf-8") as handle:
        reader = csv.reader(handle, delimiter="\t")
        try:
            return next(reader)
        except StopIteration:
            return []
