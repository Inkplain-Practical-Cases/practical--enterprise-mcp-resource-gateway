"""Transport-free handler only gets the authorized tenant from the door."""
from fastapi import HTTPException
from app.features.feature_resources.services.list_resources import list_resources, read_resource

def handle_resources(tenant: str) -> dict:
    return {"resources": list_resources(tenant)}

def handle_read(tenant: str, uri: str) -> dict:
    result = read_resource(tenant, uri)
    if result is None:
        raise HTTPException(status_code=404, detail="resource not found")
    return result
