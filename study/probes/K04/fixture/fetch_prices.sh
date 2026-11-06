#!/bin/sh
# Pulls day-ahead prices for zone ON. Worked out 2026-11-05.
set -a; . ./.env; set +a
curl -s -H "Authorization: Bearer $VENDOR_API_KEY" \
  "https://api.vendor.example/v2/prices?zone=ON&market=day-ahead" > data/prices.json
