"""Server-side filtering ensures the caller cannot enumerate other tenants."""
from app.features.feature_resources.providers.catalog import catalog

def list_resources(tenant: str) -> list[dict]:
    return [{"uri": x.uri, "description": x.description} for x in catalog() if x.tenant == tenant]

def read_resource(tenant: str, uri: str) -> dict | None:
    for x in catalog():
        if x.uri == uri and x.tenant == tenant:
            return {"uri": x.uri, "content": x.content}
    return None
