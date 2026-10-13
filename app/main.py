"""Application composition root: binds the resource feature door."""
from fastapi import FastAPI
from app.features.feature_resources.doors.router import router
app = FastAPI(title="Enterprise MCP Resource Gateway — educational offline demo")
app.include_router(router)

# Persist redacted HTTP requests and outcomes separately from MCP resource logic.
from app.core.request_audit_middleware import RequestAuditMiddleware
app.add_middleware(RequestAuditMiddleware)
