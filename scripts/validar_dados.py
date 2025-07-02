import pandas as pd
from datetime import datetime

CAMINHO_PARQUET = "../dados/silver/vendas.parquet"

def validar(df):
    erros = []

    # 1. Campos nulos
    if df.isnull().values.any():
        erros.append("❌ Existem valores nulos no dataset.")

    # 2. Valores negativos
    if (df['valor'] < 0).any():
        erros.append("❌ Existem valores negativos na coluna 'valor'.")

    # 3. Datas futuras
    if (df['data_venda'] > datetime.now()).any():
        erros.append("❌ Existem registros com data no futuro.")

    # 4. Tipos esperados
    tipos_esperados = {
        "id_venda": "int64",
        "produto": "object",
        "valor": "float64",
        "data_venda": "datetime64[ns]"
    }
    for coluna, tipo in tipos_esperados.items():
        if df[coluna].dtype != tipo:
            erros.append(f"❌ Coluna '{coluna}' está com tipo errado: {df[coluna].dtype} (esperado: {tipo})")

    # 5. IDs duplicados
    if df['id_venda'].duplicated().any():
        erros.append("❌ Existem vendas com ID duplicado.")

    return erros

# Carrega dados
try:
    df = pd.read_parquet(CAMINHO_PARQUET)
    erros = validar(df)

    if not erros:
        print("✅ Validação concluída: dados OK!")
    else:
        print("⚠️ Erros encontrados:")
        for e in erros:
            print("-", e)

except Exception as e:
    print("Erro ao carregar arquivo:", e)
