import sys
from scanner import scan_ports
from utils import classify_port

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <IP>")
        return

    ip = sys.argv[1]
    ports = scan_ports(ip)

    print(f"[+] {ip} - RESULTADO")

    if not ports:
        print("Nenhuma porta aberta encontrada.")
        return

    for port in ports:
        risk = classify_port(port)
        print(f"Porta {port} {risk}")

if __name__ == "__main__":
    main()