"""Handler maps authorized tenant context into the discovery use case."""
from app.features.feature_resources.services.discovery import discover

def handle_discovery(tenant: str) -> dict:
    return discover(tenant).model_dump()
