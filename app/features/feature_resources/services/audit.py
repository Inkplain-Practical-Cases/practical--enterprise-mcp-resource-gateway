"""Bounded audit metadata recording; never retain raw bearer credentials."""
from collections import deque
from datetime import datetime, timezone

_EVENTS: deque[dict] = deque(maxlen=1000)

def record_event(operation: str, tenant: str, outcome: str) -> None:
    """Append redacted, finite-size evidence; production uses durable storage."""
    _EVENTS.append({"operation":operation,"tenant":tenant,"outcome":outcome,"at":datetime.now(timezone.utc).isoformat()})

def audit_snapshot() -> list[dict]:
    return list(_EVENTS)
