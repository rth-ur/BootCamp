from scanner import scan_ports, scan_network
from utils import classify_port
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <base_ip>")
        return

    base_ip = sys.argv[1]

    print("[*] Escaneando rede...")

    hosts = scan_network(base_ip)

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