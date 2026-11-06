# OPERATIONS.md

## Resource inventory

- **pi-ingest** — 192.168.1.40; runs `src/ingest.py` under systemd unit `ingest.service`.

## Access

- **pi-ingest** — `ssh pi-ingest` (alias in `~/.ssh/config`); user `ops`; key auth.

## Credential locations

- Utility API token: `~/.config/meters/token` on pi-ingest.
