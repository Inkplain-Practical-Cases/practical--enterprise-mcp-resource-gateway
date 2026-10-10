"""Structured discovery response for transport-independent MCP-style clients."""
from pydantic import BaseModel

class Discovery(BaseModel):
    protocol: str
    capabilities: list[str]
    resources: list[dict]
