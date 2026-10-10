"""Confirm sensitive bearer token never appears in audit snapshots."""
from fastapi.testclient import TestClient
from app.main import app
from app.features.feature_resources.services.audit import audit_snapshot
client=TestClient(app)
AUTH={"Authorization":"Bearer local-reader","X-Tenant":"acme"}

def test_redacted_audit():
    client.post("/tools/purchase-order",json={"order_id":"po-42"},headers=AUTH)
    assert any(x["operation"]=="purchase_order_read" for x in audit_snapshot())
    assert "local-reader" not in str(audit_snapshot())
