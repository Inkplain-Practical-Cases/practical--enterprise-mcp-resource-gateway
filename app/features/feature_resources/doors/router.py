"""Resource and discovery HTTP doors: identity is verified on each request."""
from fastapi import APIRouter, Header
from app.features.feature_resources.services.authorization import authorize
from app.features.feature_resources.handlers.handle_resources import handle_resources, handle_read
from app.features.feature_resources.handlers.handle_discovery import handle_discovery
router = APIRouter()

@router.get("/resources")
def resources(x_tenant: str = Header(default=""), authorization: str = Header(default="")) -> dict:
    return handle_resources(authorize(authorization, x_tenant))

@router.get("/resource")
def resource(uri: str, x_tenant: str = Header(default=""), authorization: str = Header(default="")) -> dict:
    return handle_read(authorize(authorization, x_tenant), uri)

@router.get("/discover")
def discovery(x_tenant: str = Header(default=""), authorization: str = Header(default="")) -> dict:
    return handle_discovery(authorize(authorization, x_tenant))
