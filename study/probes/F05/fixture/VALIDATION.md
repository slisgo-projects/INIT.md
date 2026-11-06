# VALIDATION.md

## Phase 1 — Ingest

- V1: one CSV file per hour in `data/raw/`. Check: `tests/test_files.py`.
- V2: columns `timestamp`, `meter_id`, `load_kw`. Check: `tests/test_columns.py`.
- V3: 24 h soak run against the live utility API without gaps. Check: `scripts/soak.sh`.
