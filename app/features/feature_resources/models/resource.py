"""Typed synthetic resource contracts; no customer records are used."""
from pydantic import BaseModel, Field

class Resource(BaseModel):
    uri: str = Field(pattern=r"^enterprise://[a-z-]+/[a-z0-9-]+$")
    tenant: str
    content: str
    description: str
