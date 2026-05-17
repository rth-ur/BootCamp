import os
import sys
import socket
import streamlit as st
import requests

# Ajuste dinâmico de caminhos para funcionamento local e na nuvem
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from utils import classify_port

st.set_page_config(page_title="NetSafe Web", page_icon="🛡️", layout="centered")

st.title("🛡️ NetSafe - Verificador de Segurança de Redes")
st.markdown("Uma ferramenta web para analisar o contexto do seu IP público e verificar vulnerabilidades de portas expostas.")

# 1. Integração com a API Pública de Geolocalização (Exigência 1.2)
st.subheader("🌐 Passo 1: Informações de Geolocalização do seu IP")
st.markdown("Clique no botão abaixo para consumir a API externa e identificar os dados de rede do seu provedor.")

if st.button("Buscar Dados do IP Externo"):
    try:
        response = requests.get("https://ipapi.co/json/", timeout=5)
        if response.status_code == 200:
            dados = response.json()
            st.success("Dados obtidos da API pública com sucesso!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Seu IP Público", dados.get("ip"))
                st.write(f"**Cidade:** {dados.get('city')}")
                st.write(f"**Região:** {dados.get('region')}")
            with col2:
                st.write(f"**País:** {dados.get('country_name')}")
                st.write(f"**Provedor (ISP):** {dados.get('org')}")
        else:
            st.error("A API externa retornou um erro de resposta.")
    except Exception:
        st.error("Falha na conexão com a API externa (Timeout/Conexão).")

st.markdown("---")

# 2. Funcionalidade de Port Scan adaptada para Ambiente Web Cloud
st.subheader("🔍 Passo 2: Verificação de Portas Públicas (Port Scan)")
st.info("Nota técnica: Como a aplicação está rodando na nuvem, o scanner testará conexões públicas com o IP ou domínio informado.")

alvo = st.text_input("Digite um domínio ou IP Público para testar (Ex: google.com ou o seu próprio IP público):", "")
portas_input = st.text_input("Portas para testar (separadas por vírgula):", "21,22,23,80,443,3389")

if st.button("Iniciar Análise de Portas"):
    if not alvo:
        st.warning("Por favor, insira um endereço IP ou Domínio válido.")
    else:
        try:
            ip_alvo = socket.gethostbyname(alvo)
            st.write(f"Analisando o alvo: **{alvo}** ({ip_alvo})")
            
            portas = [int(p.strip()) for p in portas_input.split(",") if p.strip().isdigit()]
            portas_abertas = []
            
            progresso = st.progress(0)
            
            for idx, porta in enumerate(portas):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1.0)
                result = sock.connect_ex((ip_alvo, porta))
                if result == 0:
                    portas_abertas.append(porta)
                sock.close()
                progresso.progress((idx + 1) / len(portas))
                
            if portas_abertas:
                st.warning(f"⚠️ Portas expostas encontradas: {portas_abertas}")
                for p in portas_abertas:
                    risk = classify_port(p)
                    if risk:
                        st.error(f"Porta {p}: {risk}")
                    else:
                        st.info(f"Porta {p}: Aberta (Sem classificação de risco mapeada).")
            else:
                st.success("✅ Nenhuma das portas especificadas está aberta publicamente neste alvo.")
                
        except socket.gaierror:
            st.error("❌ Não foi possível resolver o domínio ou IP informado. Verifique a digitação.")
        except Exception as e:
            st.error(f"❌ Ocorreu um erro durante a execução: {e}")