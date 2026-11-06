"""Ingest: hourly meter readings -> data/raw/*.csv. Output contract: INTERFACES.md IF-01."""
import csv
from datetime import datetime, timezone


def write_hour(rows, path):
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["timestamp", "meter_id", "load_kw"])
        for ts, meter, kw in rows:
            w.writerow([datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), meter, kw])
