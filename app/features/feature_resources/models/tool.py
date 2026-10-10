"""Strict typed tool input: forbid unknown keys to block accidental privilege changes."""
from pydantic import BaseModel, ConfigDict, Field

class PurchaseOrderQuery(BaseModel):
    model_config = ConfigDict(extra="forbid")
    order_id: str = Field(pattern=r"^po-[0-9]{1,6}$")

class PurchaseOrderResult(BaseModel):
    order_id: str
    status: str
    tenant: str
