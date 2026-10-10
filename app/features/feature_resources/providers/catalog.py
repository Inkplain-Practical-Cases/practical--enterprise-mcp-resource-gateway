"""In-memory fixture provider keeps learning steps independent of live MCP accounts."""
from app.features.feature_resources.models.resource import Resource

CATALOG = (
    Resource(uri="enterprise://policy/vendor", tenant="acme", content="Approved vendors require compliance review.", description="Vendor policy"),
    Resource(uri="enterprise://orders/po-42", tenant="acme", content="PO-42 is approved.", description="Synthetic PO"),
    Resource(uri="enterprise://policy/vendor-b", tenant="beta", content="Beta tenant only.", description="Private policy"),
)

def catalog() -> tuple[Resource, ...]:
    """Return immutable collection; authorization is added in a later step."""
    return CATALOG
