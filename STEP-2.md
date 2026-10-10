# STEP-2 of 6 — MCP resource endpoints with authorization

## What changes
This cumulative branch adds authorization behavior. Follow the door → handler → service → provider layers and use synthetic fixture inputs only.

## Run and verify
```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Component contracts
Read STEP-2.crd alongside the source and test files. Refused access must not leak other tenants' resources.

## Next
STEP-3: Client discovery and session transport
