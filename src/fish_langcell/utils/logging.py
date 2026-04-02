"""Structured logging helpers."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from typing import Any


def setup_logger(name: str = "fish_langcell", level: int = logging.INFO) -> logging.Logger:
    """Create or fetch a configured logger."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def log_event(logger: logging.Logger, event: str, **payload: Any) -> None:
    """Emit a JSON-serializable log event."""
    record = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "event": event,
        **payload,
    }
    logger.info(json.dumps(record, ensure_ascii=False))
