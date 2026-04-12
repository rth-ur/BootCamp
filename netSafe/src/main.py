from scanner import scan_ports, scan_network
from utils import classify_port
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <base_ip>")
        print("Exemplo: python main.py 192.168.1")
        return

    base_ip = sys.argv[1]
    
    partes_ip = base_ip.split('.')
    if len(partes_ip) != 3:
        print("\n[!] ERRO: Formato de IP inválido!")
        print("[!] Deves inserir apenas os 3 primeiros blocos (octetos) da rede.")
        print("[!] Correto: 192.168.1")
        print("[!] Incorreto: 192.168.1.15\n")
        return
    
    print(f"[*] A explorar a rede {base_ip}.X ...")

    hosts = scan_network(base_ip)

   
    if not hosts:
        print("[-] Nenhum dispositivo ativo encontrado nesta rede.")
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