# STEP-6 of 6 — Integration tests CI and hardening

## What changes
This cumulative branch adds integration behavior. Follow the door → handler → service → provider layers and use synthetic fixture inputs only.

## Run and verify
```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Component contracts
Read STEP-6.crd alongside the source and test files. Refused access must not leak other tenants' resources.

## Next
Promote this tested code to main and inspect FINAL.crd.

## Database (Entity) Relations
The MCP gateway persists redacted HTTP request/outcome audit in SQLite. See STEP-6.erd and STEP-6-ERD.
