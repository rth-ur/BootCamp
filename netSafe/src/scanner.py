import socket
import subprocess

COMMON_PORTS = [21, 22, 23, 80, 443, 3389]


def scan_ports(ip):
    open_ports = []

    for port in COMMON_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)

        sock.close()

    return open_ports


def ping_host(ip):
    try:
        output = subprocess.run(
            ["ping", "-n", "1", "-w", "500", ip],
            stdout=subprocess.DEVNULL
        )
        return output.returncode == 0
    except Exception:
        return False


def scan_network(base_ip):
    active_hosts = []

    for i in range(1, 255):
        ip = f"{base_ip}.{i}"
        if ping_host(ip):
            active_hosts.append(ip)

    return active_hosts