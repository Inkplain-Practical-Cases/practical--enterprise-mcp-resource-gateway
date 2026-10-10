"""Only a validated request reaches the single approved query tool."""
from app.features.feature_resources.models.tool import PurchaseOrderQuery
from app.features.feature_resources.services.tool_query import query_purchase_order

def handle_tool(tenant: str, query: PurchaseOrderQuery) -> dict:
    return query_purchase_order(tenant, query).model_dump()
