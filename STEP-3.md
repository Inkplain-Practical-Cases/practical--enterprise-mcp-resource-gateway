# STEP-3 of 6 — Client discovery and session transport

## What changes
This cumulative branch adds discovery behavior. Follow the door → handler → service → provider layers and use synthetic fixture inputs only.

## Run and verify
```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Component contracts
Read STEP-3.crd alongside the source and test files. Refused access must not leak other tenants' resources.

## Next
STEP-4: Typed tool schemas and validated outputs
