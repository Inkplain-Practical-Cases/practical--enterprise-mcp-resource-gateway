"""End-to-end negative and happy paths through the HTTP boundary."""
from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
A={"Authorization":"Bearer local-reader","X-Tenant":"acme"}

def test_full_resource_flow():
    names=[x["uri"] for x in client.get("/discover",headers=A).json()["resources"]]
    assert "enterprise://orders/po-42" in names
    assert client.get("/resource",params={"uri":names[0]},headers=A).status_code==200
    assert client.post("/tools/purchase-order",json={"order_id":"po-42"},headers=A).json()["status"]=="approved"

def test_fail_closed():
    assert client.get("/discover",headers={"Authorization":"Bearer invalid","X-Tenant":"acme"}).status_code==401
    assert client.get("/resource",params={"uri":"enterprise://policy/vendor-b"},headers=A).status_code==404
    assert client.post("/tools/purchase-order",json={"order_id":"bad"},headers=A).status_code==422
