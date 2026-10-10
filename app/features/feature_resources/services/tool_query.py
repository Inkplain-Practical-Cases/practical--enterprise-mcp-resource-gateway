"""Allowlisted, read-only synthetic tool; every output has a typed schema."""
from app.features.feature_resources.models.tool import PurchaseOrderQuery, PurchaseOrderResult

def query_purchase_order(tenant: str, query: PurchaseOrderQuery) -> PurchaseOrderResult:
    status = "approved" if query.order_id == "po-42" else "not_found"
    return PurchaseOrderResult(order_id=query.order_id, status=status, tenant=tenant)
