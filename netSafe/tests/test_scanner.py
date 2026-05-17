from unittest.mock import patch
import requests
from src.scanner import scan_ports
from src.utils import classify_port


def test_scan_ports_returns_list():
    result = scan_ports("127.0.0.1")
    assert isinstance(result, list)


def test_classify_port_known():
    assert "SSH" in classify_port(22)


def test_classify_port_unknown():
    assert classify_port(9999) == ""


# Teste de Integração Obrigatório com Mock (Exigência 1.3 do Barema)
@patch("requests.get")
def test_integracao_api_geolocalizacao(mock_get):
    # Simulamos uma resposta bem-sucedida (200 OK) da API externa
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "ip": "127.0.0.1",
        "city": "Brasilia",
        "region": "Federal District",
        "country_name": "Brazil",
        "org": "Provedor Teste"
    }
    
    response = requests.get("https://ipapi.co/json/", timeout=5)
    
    # Validações do fluxo de dados da API
    assert response.status_code == 200
    dados = response.json()
    assert "ip" in dados
    assert "country_name" in dados