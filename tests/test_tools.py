"""Reject unknown tool args and validate deterministic PO results."""
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
AUTH={"Authorization":"Bearer local-reader","X-Tenant":"acme"}

def test_typed_tool():
    r=client.post("/tools/purchase-order",json={"order_id":"po-42"},headers=AUTH)
    assert r.status_code==200 and r.json()["status"]=="approved"

def test_invalid_tool_args():
    assert client.post("/tools/purchase-order",json={"order_id":"../../etc/passwd"},headers=AUTH).status_code==422
    assert client.post("/tools/purchase-order",json={"order_id":"po-42","tenant":"beta"},headers=AUTH).status_code==422
