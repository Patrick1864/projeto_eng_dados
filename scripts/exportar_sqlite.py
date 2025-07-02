import pandas as pd
from sqlalchemy import create_engine
import os

CAMINHO_PARQUET = "../dados/silver/vendas.parquet"
CAMINHO_DB = "../dados/sqlite/vendas.db"

# Garante que a pasta exista
os.makedirs(os.path.dirname(CAMINHO_DB), exist_ok=True)

# Lê os dados
df = pd.read_parquet(CAMINHO_PARQUET)

# Cria conexão com o SQLite
engine = create_engine(f"sqlite:///{CAMINHO_DB}")

# Insere na tabela "vendas"
try:
    df.to_sql("vendas", engine, index=False, if_exists="replace")
    print(f"✅ {len(df)} registros inseridos no SQLite com sucesso!")
except Exception as e:
    print("❌ Erro ao inserir dados:", e)
