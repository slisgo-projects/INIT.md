# INTERFACES.md

- **IF-01 Ingest → Store**
  - Direction: Ingest → Store.
  - Contract: Parquet files, one per hour, in `data/raw/`; columns `timestamp` (UTC ISO 8601), `meter_id`, `load_kw`.
  - Status: active.
- **IF-02 Store → Dashboard**
  - Direction: Store → Dashboard.
  - Contract: SQL view `daily_load` (`date`, `meter_id`, `kwh`).
  - Status: active.
