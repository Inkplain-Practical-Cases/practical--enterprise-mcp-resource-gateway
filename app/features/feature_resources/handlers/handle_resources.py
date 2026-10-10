"""HTTP handler delegates business work to one service."""
from app.features.feature_resources.services.list_resources import list_resources

def handle_resources() -> dict:
    """Keep transport serialization outside the provider."""
    return {"resources": list_resources()}
