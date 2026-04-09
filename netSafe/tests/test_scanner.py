from src.scanner import scan_ports

def test_scan_ports_returns_list():
    result = scan_ports("127.0.0.1")
    assert isinstance(result, list)