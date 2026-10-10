"""Discovery must preserve tenant boundaries and bounded capability metadata."""
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
AUTH={"Authorization":"Bearer local-reader","X-Tenant":"acme"}

def test_discovery():
    result=client.get("/discover",headers=AUTH)
    assert result.status_code==200
    assert result.json()["capabilities"]==["resources/list","resources/read"]
    assert len(result.json()["resources"])==2

def test_discovery_denied():
    assert client.get("/discover").status_code==401
