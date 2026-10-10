"""FastAPI door owns HTTP routing, not business policy."""
from fastapi import APIRouter
from app.features.feature_resources.handlers.handle_resources import handle_resources
router = APIRouter()

@router.get("/resources")
def resources() -> dict:
    """Read synthetic catalog via handler/service/provider chain."""
    return handle_resources()
