# STEP-5 of 6 — Auditing and error boundaries

## What changes
This cumulative branch adds audit behavior. Follow the door → handler → service → provider layers and use synthetic fixture inputs only.

## Run and verify
```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

## Component contracts
Read STEP-5.crd alongside the source and test files. Refused access must not leak other tenants' resources.

## Next
STEP-6: Integration tests CI and hardening
