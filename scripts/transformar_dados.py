import pandas as pd
import os

CAMINHO_ENTRADA = "../dados/bronze/vendas.json"
CAMINHO_SAIDA = "../dados/silver/vendas.parquet"

# Garante que a pasta existe
os.makedirs(os.path.dirname(CAMINHO_SAIDA), exist_ok=True)

# Leitura dos dados JSON
df = pd.read_json(CAMINHO_ENTRADA, lines=True)

# Conversões e limpeza
df['data_venda'] = pd.to_datetime(df['data_venda'])

# Salvar como Parquet
df.to_parquet(CAMINHO_SAIDA, index=False)

print(f"{len(df)} registros processados e salvos em formato Parquet.")
