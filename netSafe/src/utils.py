def classify_port(port):
    risks = {
        21: "FTP ⚠️",
        22: "SSH ⚠️",
        23: "TELNET 🔥",
        3389: "RDP ⚠️"
    }
    return risks.get(port, "")