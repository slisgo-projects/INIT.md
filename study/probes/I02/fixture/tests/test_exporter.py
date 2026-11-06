from src.exporter import export_csv


def test_export_header():
    assert export_csv([]).startswith("timestamp")
