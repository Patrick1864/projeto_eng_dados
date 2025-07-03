"""
Projeto de Engenharia de Dados com Python, Pandas, Streamlit e SQLite
======================================================================

📌 Objetivo:
------------
Este projeto simula um pipeline completo de engenharia de dados,
processando e monitorando dados de vendas em tempo quase real.

🎯 Etapas:
----------
1. Geração de dados simulados em JSON (camada Bronze)
2. Transformação e padronização com Pandas (camada Silver - Parquet)
3. Validação de dados (nulos, negativos, duplicados, etc)
4. Exportação para banco de dados local SQLite
5. Visualização interativa com Streamlit (dashboard em tempo real)
6. Pipeline contínuo com alertas de vendas baixas

🧰 Tecnologias Utilizadas:
---------------------------
- Python 3.9+
- Pandas
- PyArrow
- SQLite (via SQLAlchemy)
- Streamlit
- Subprocess (para automação)
- Validação customizada em Python

📊 Funcionalidades do Dashboard:
-------------------------------
- Filtros por data e produto
- KPIs: total vendido e ticket médio
- Gráficos de vendas por dia e por produto
- Alertas em tempo real para queda de vendas
- Atualização automática a cada X segundos

📁 Estrutura de Diretórios:
---------------------------
projeto_eng_dados/
├── dados/
│   ├── bronze/         # Dados brutos (JSON)
│   ├── silver/         # Dados tratados (Parquet)
│   └── sqlite/         # Banco SQLite
├── dashboard/
│   └── dashboard_streamlit.py
├── scripts/
│   ├── gerar_dados.py
│   ├── transformar_dados.py
│   ├── exportar_sqlite.py
│   ├── validar_dados.py
│   ├── pipeline_automatico.py
│   └── pipeline_loop.py

🚀 Como executar:
-----------------
1. Gerar dados e rodar pipeline completo:
   $ python scripts/pipeline_automatico.py

2. Rodar o dashboard:
   $ streamlit run dashboard/dashboard_streamlit.py

3. Rodar o pipeline contínuo (simulação real-time):
   $ python scripts/pipeline_loop.py
