from src.scanner import scan_ports
from src.utils import classify_port


def test_scan_ports_returns_list():
    result = scan_ports("127.0.0.1")
    assert isinstance(result, list)


def test_classify_port_known():
    assert "SSH" in classify_port(22)


def test_classify_port_unknown():
    assert classify_port(9999) == ""