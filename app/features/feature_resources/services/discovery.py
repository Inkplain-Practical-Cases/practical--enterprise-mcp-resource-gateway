"""Build a bounded session discovery response from the authorized resource list."""
from app.features.feature_resources.services.list_resources import list_resources
from app.features.feature_resources.models.discovery import Discovery

def discover(tenant: str) -> Discovery:
    return Discovery(protocol="educational-mcp-style-v1", capabilities=["resources/list", "resources/read"], resources=list_resources(tenant))
