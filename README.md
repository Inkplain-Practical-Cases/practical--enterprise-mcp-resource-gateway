# Enterprise MCP Resource Gateway

A **deterministic, MCP-inspired learning reference**, not a protocol-compliant remote MCP server or deployable enterprise identity service. All records, credentials and policies in this exercise are synthetic.

## Learn in six cumulative Git branches
1. Resource catalog and access-scoped data model
2. MCP resource endpoints with authorization
3. Client discovery and session transport (HTTP teaching analogue)
4. Typed tool schemas and validated outputs
5. Auditing and error boundaries
6. Integration tests, CI and hardening

Each branch contains its corresponding `STEP-N.crd`, `STEP-N.md` and runnable tests. Check out each branch in order. Main holds the final application.

## Run
```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -q
python -m uvicorn app.main:app --reload
```
Uvicorn must be installed separately to run the HTTP server in this version. Tests use FastAPI TestClient directly. For authenticated requests use **synthetic local-only** headers `Authorization: Bearer local-reader` and `X-Tenant: acme`. Never reuse that literal credential in deployed services.

## What this omits
No real MCP JSON-RPC initialize/session lifecycle, OAuth JWT validation, durable audit store, multi-process concurrency, real provider timeouts, secret management or production observability. Use the step CRDs and the final INKP simulator to explain these boundaries, not to assert their production readiness.
