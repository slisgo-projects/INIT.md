# ARCHITECTURE.md

## Elements

- **Ingest** — pulls hourly meter readings from the utility API; writes one CSV file per hour to `data/raw/`.
  - Depends on: utility API.
- **Store** — loads the hourly Parquet files in `data/raw/` into the analysis database.
  - Depends on: Ingest.
- **Dashboard** — renders daily load charts from the database.
  - Depends on: Store.
