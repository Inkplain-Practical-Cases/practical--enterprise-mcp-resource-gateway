"""Four explicit request doors, never a free-form tool dispatcher."""
from fastapi import APIRouter, Header
from app.features.feature_resources.models.tool import PurchaseOrderQuery
from app.features.feature_resources.services.authorization import authorize
from app.features.feature_resources.handlers.handle_resources import handle_resources, handle_read
from app.features.feature_resources.handlers.handle_discovery import handle_discovery
from app.features.feature_resources.handlers.handle_tool import handle_tool
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

@router.post("/tools/purchase-order")
def purchase_order(query: PurchaseOrderQuery, x_tenant: str = Header(default=""), authorization: str = Header(default="")) -> dict:
    return handle_tool(authorize(authorization, x_tenant), query)
