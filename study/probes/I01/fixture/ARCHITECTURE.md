# ARCHITECTURE.md

## Elements

- **Ingest** — pulls hourly meter readings from the utility API; writes CSV files to `data/raw/`.
  - Depends on: utility API.
- **Store** — loads files from `data/raw/` into the analysis database.
  - Depends on: Ingest.
- **Dashboard** — renders daily load charts from the database.
  - Depends on: Store.
