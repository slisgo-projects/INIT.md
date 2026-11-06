from src.ingest import fetch


def test_fetch_empty():
    assert fetch("m1") == []
