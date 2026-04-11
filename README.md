# NetSafe - Verificador de Segurança de Redes Domésticas

[![CI](https://github.com/rth-ur/BootCamp/actions/workflows/ci.yml/badge.svg)](https://github.com/rth-ur/BootCamp/actions/workflows/ci.yml)

**Versão:** 1.0.0

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

### 1. Clone o repositório:
```bash
git clone [https://github.com/rth-ur/BootCamp.git](https://github.com/rth-ur/BootCamp.git)
```

### 2. Acesse a pasta raiz do projeto:
```bash
cd BootCamp
```

### 3. Crie e ative um ambiente virtual:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🚀 Como Executar
Com o ambiente virtual ativado na raiz do projeto, execute o script principal passando o IP base da sua rede. Exemplo:
```bash
python netSafe/src/main.py 192.168.1
```

## 🧪 Como Rodar os Testes
Para garantir que o código está funcionando como esperado e cobrindo os cenários de uso (via Pytest), execute o comando abaixo na raiz do projeto:
```bash
python -m pytest netSafe/
```

## 🧹 Como Rodar o Linting
Para verificar a padronização e a qualidade estática do código (via Ruff), execute:
```bash
python -m ruff check .
```

## 👨‍💻 Autor e Repositório
- **Autor:** Arthur Clemente
- **Repositório Público:** https://github.com/rth-ur/BootCamp