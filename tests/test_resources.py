"""Offline regression checks: no credentials or network services required."""
from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_catalog_returns_synthetic_metadata():
    result = client.get("/resources")
    assert result.status_code == 200
    assert len(result.json()["resources"]) == 3
