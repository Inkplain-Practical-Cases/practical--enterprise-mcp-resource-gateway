"""Tenant-scope and missing-credential regression tests."""
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)
AUTH = {"Authorization": "Bearer local-reader", "X-Tenant": "acme"}

def test_catalog_requires_auth():
    assert client.get("/resources").status_code == 401

def test_scoped_catalog():
    response = client.get("/resources", headers=AUTH)
    assert response.status_code == 200
    assert len(response.json()["resources"]) == 2

def test_cross_tenant_is_denied():
    assert client.get("/resources", headers={**AUTH, "X-Tenant": "beta"}).status_code == 403

def test_cross_tenant_resource_is_hidden():
    assert client.get("/resource", params={"uri":"enterprise://policy/vendor-b"}, headers=AUTH).status_code == 404
