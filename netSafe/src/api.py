from flask import Flask, request, jsonify, render_template
from scanner import scan_ports, scan_network
from utils import classify_port

app = Flask(__name__)

@app.route('/')
def index():
    # Serve a página HTML principal
    return render_template('index.html')

@app.route('/api/scan', methods=['POST'])
def scan():
    data = request.json
    base_ip = data.get('base_ip')

    if not base_ip or len(base_ip.split('.')) != 3:
        return jsonify({"error": "Formato de IP inválido. Ex: 192.168.1"}), 400

    hosts_found = []
    
    # Usa as funções já existentes no seu projeto para mapear a rede
    active_hosts = scan_network(base_ip)

    for ip in active_hosts:
        open_ports = scan_ports(ip)
        ports_info = []
        for port in open_ports:
            ports_info.append({
                "port": port,
                "risk": classify_port(port)
            })

        hosts_found.append({
            "ip": ip,
            "ports": ports_info
        })

    return jsonify({"base_ip": base_ip, "hosts": hosts_found})

if __name__ == '__main__':
    # host='0.0.0.0' permite que a API seja acedida por qualquer dispositivo na mesma rede
    app.run(host='0.0.0.0', debug=True, port=5000)