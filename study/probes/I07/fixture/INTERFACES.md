# INTERFACES.md

- **IF-01 Ingest → Store**
  - Direction: Ingest → Store.
  - Contract: CSV, one file per hour in `data/raw/`; columns `timestamp` (UTC, ISO 8601 with `Z`), `meter_id`, `load_kw`.
  - Owner: Ingest side — operator; Store side — operator.
  - Status: active.
