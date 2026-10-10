"""List resources through an injected data-provider boundary."""
from app.features.feature_resources.providers.catalog import catalog

def list_resources() -> list[dict]:
    """Expose basic metadata while still in the offline starter slice."""
    return [{"uri": item.uri, "description": item.description} for item in catalog()]
