# NetSafe - Verificador de Segurança de Redes Domésticas

## 📌 Descrição do Problema
Muitas pessoas utilizam redes Wi-Fi domésticas sem saber quais dispositivos estão conectados ou quais portas estão abertas. Isso pode representar riscos de segurança, como acesso não autorizado ou exposição de serviços sensíveis.

## 💡 Proposta da Solução
O NetSafe é uma ferramenta simples em linha de comando (CLI) que permite ao usuário escanear sua rede local, identificar dispositivos ativos e verificar portas abertas, fornecendo uma visão básica da segurança da rede.

## 👥 Público-Alvo
- Usuários domésticos
- Estudantes de tecnologia
- Pessoas interessadas em segurança básica de redes

## ⚙️ Funcionalidades
- Descoberta de dispositivos na rede (scan de IP)
- Verificação de portas abertas
- Classificação básica de risco (ex: Telnet inseguro)
- Execução via linha de comando (CLI)

## 🛠️ Tecnologias Utilizadas
- Python 3
- Socket (rede)
- Subprocess (ping)
- Pytest (testes)
- Ruff (lint)

## 📥 Instalação

```bash
git clone https://github.com/rth-ur/BootCamp.git
cd BootCamp/netSafe
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
