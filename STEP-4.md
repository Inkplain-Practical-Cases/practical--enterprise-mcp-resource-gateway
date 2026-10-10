# STEP-4 of 6 — Typed tool schemas and validated outputs

## What changes
This cumulative branch adds tool behavior. Follow the door → handler → service → provider layers and use synthetic fixture inputs only.

## Run and verify
```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Component contracts
Read STEP-4.crd alongside the source and test files. Refused access must not leak other tenants' resources.

## Next
STEP-5: Auditing and error boundaries
