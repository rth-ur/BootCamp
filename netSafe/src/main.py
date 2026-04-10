from scanner import scan_ports, scan_network
from utils import classify_port
import sys

__version__ = "1.0.0"

def main():
    print(f"--- NetSafe Scanner v{__version__} ---")
    if len(sys.argv) < 2:
        print("Uso: python main.py <ip_alvo>")
        return

    alvo_ip = sys.argv[1]
    
    partes = alvo_ip.split('.')
    if len(partes) == 4:
        base_ip = f"{partes[0]}.{partes[1]}.{partes[2]}"
    else:
        base_ip = alvo_ip

    print(f"[*] Escaneando rede base: {base_ip}.X ... (Pode demorar 1 ou 2 minutos)")

    hosts = scan_network(base_ip)

    if not hosts:
        print("[-] Nenhum dispositivo ativo encontrado. Tente outro IP.")
        return

    for ip in hosts:
        print(f"\n[+] {ip} - ATIVO")
        ports = scan_ports(ip)

        if not ports:
            print("Sem portas abertas")
            continue

        for port in ports:
            risk = classify_port(port)
            print(f"Porta {port} {risk}")

if __name__ == "__main__":
    main()