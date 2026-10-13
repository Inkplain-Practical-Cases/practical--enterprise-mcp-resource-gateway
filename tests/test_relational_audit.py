"""Test HTTP request/event FK constraints for MCP resource gateway telemetry."""
import sqlite3
from app.providers.provider_record_request_audit import provider_record_request_audit

def test_mcp_gateway_audit(tmp_path):
    path=str(tmp_path/"mcp.sqlite3")
    request_id=provider_record_request_audit("GET","/resources",200,10.2,path)
    with sqlite3.connect(path) as con:
        assert con.execute("SELECT COUNT(*) FROM mcp_api_requests WHERE id=?",(request_id,)).fetchone()[0]==1
        assert con.execute("SELECT COUNT(*) FROM mcp_api_events WHERE request_id=?",(request_id,)).fetchone()[0]==1
        assert con.execute("PRAGMA foreign_key_check").fetchall()==[]
