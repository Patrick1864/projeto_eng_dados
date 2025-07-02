import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import os
import time

CAMINHO_DB = "../dados/sqlite/vendas.db"

st.set_page_config(page_title="Dashboard de Vendas em Tempo Real", layout="wide")
st.title("📊 Dashboard de Vendas com Alertas em Tempo Real")

# Atualização automática
tempo_refresh = st.sidebar.number_input("⏱️ Atualizar a cada (segundos):", min_value=5, max_value=300, value=30, step=5)

# Corrigido: função auxiliar para botão
def atualizar():
    st.experimental_rerun()

st.sidebar.button("🔄 Atualizar agora", on_click=atualizar)

st.sidebar.markdown(f"<small>Última atualização: {datetime.now().strftime('%H:%M:%S')}</small>", unsafe_allow_html=True)

if not os.path.exists(CAMINHO_DB):
    st.warning("❗ Banco de dados não encontrado.")
    st.stop()

# Carrega dados do SQLite
engine = create_engine(f"sqlite:///{CAMINHO_DB}")
df = pd.read_sql("SELECT * FROM vendas", engine)

df['data_venda'] = pd.to_datetime(df['data_venda'])

# Filtros
st.sidebar.header("Filtros")
data_inicio = st.sidebar.date_input("Data Início", df['data_venda'].min().date())
data_fim = st.sidebar.date_input("Data Fim", df['data_venda'].max().date())
produtos = st.sidebar.multiselect("Produtos", df['produto'].unique(), default=df['produto'].unique())

# Aplica filtros
df = df[(df['data_venda'].dt.date >= data_inicio) & (df['data_venda'].dt.date <= data_fim)]
df = df[df['produto'].isin(produtos)]

# ALERTA de vendas baixas
vendas_ultimos_10 = df.tail(10)['valor'].sum()
if vendas_ultimos_10 < 1000:
    st.error(f"🚨 Alerta: vendas baixas nos últimos 10 registros! Total: R$ {vendas_ultimos_10:.2f}")
else:
    st.success(f"✅ Vendas saudáveis! Total últimos 10 registros: R$ {vendas_ultimos_10:.2f}")

# KPIs
col1, col2 = st.columns(2)
col1.metric("💰 Ticket Médio", f"R$ {df['valor'].mean():.2f}")
col2.metric("📦 Total Vendido", f"R$ {df['valor'].sum():.2f}")

# Gráfico de vendas por dia
st.subheader("📈 Vendas por Dia")
vendas_dia = df.groupby(df['data_venda'].dt.date)['valor'].sum().reset_index()
st.line_chart(vendas_dia.set_index("data_venda"))

# Gráfico de vendas por produto
st.subheader("📊 Vendas por Produto")
vendas_prod = df.groupby("produto")["valor"].sum().reset_index()
st.bar_chart(vendas_prod.set_index("produto"))

# Tabela
st.subheader("📋 Últimos Registros")
st.dataframe(df.tail(10))

# Atualização automática
time.sleep(tempo_refresh)
st.experimental_rerun()
