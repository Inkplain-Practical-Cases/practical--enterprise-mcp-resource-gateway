# STEP-1 of 6 — Resource catalog and access-scoped data model

## What changes
This cumulative branch adds catalog behavior. Follow the door → handler → service → provider layers and use synthetic fixture inputs only.

## Run and verify
```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Component contracts
Read STEP-1.crd alongside the source and test files. Refused access must not leak other tenants' resources.

## Next
STEP-2: MCP resource endpoints with authorization
