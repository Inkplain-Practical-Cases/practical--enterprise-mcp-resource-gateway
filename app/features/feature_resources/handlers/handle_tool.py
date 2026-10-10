"""Record both successful and failed tool calls without leaking credentials."""
from app.features.feature_resources.models.tool import PurchaseOrderQuery
from app.features.feature_resources.services.tool_query import query_purchase_order
from app.features.feature_resources.services.audit import record_event

def handle_tool(tenant: str, query: PurchaseOrderQuery) -> dict:
    try:
        result=query_purchase_order(tenant,query)
        record_event("purchase_order_read",tenant,result.status)
        return result.model_dump()
    except Exception:
        record_event("purchase_order_read",tenant,"failed")
        raise
