import json

LIMIT_MS = 50


def test_p95_latency():
    p95 = json.load(open("results/latency.json"))["p95_ms"]
    assert p95 < LIMIT_MS, f"p95 {p95} ms >= {LIMIT_MS} ms"
