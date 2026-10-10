"""Fail-closed tenant and bearer-token checks; demo identity only."""
from fastapi import HTTPException

def authorize(token: str, tenant: str) -> str:
    """Resolve a fixed demo identity, never trusting the requested tenant alone."""
    if token != "Bearer local-reader":
        raise HTTPException(status_code=401, detail="invalid credentials")
    if tenant != "acme":
        raise HTTPException(status_code=403, detail="tenant scope denied")
    return tenant
