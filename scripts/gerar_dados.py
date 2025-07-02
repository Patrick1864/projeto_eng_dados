import random
import time
import json
from datetime import datetime
import os

CAMINHO_SAIDA = "../dados/bronze/vendas.json"

# Garante que a pasta existe
os.makedirs(os.path.dirname(CAMINHO_SAIDA), exist_ok=True)

def gerar_venda():
    return {
        "id_venda": random.randint(1000, 9999),
        "produto": random.choice(["Camisa", "Tênis", "Boné", "Calça"]),
        "valor": round(random.uniform(50, 500), 2),
        "data_venda": datetime.now().isoformat()
    }

# Gerar 1 venda a cada 2 segundos
while True:
    venda = gerar_venda()
    with open(CAMINHO_SAIDA, "a") as f:
        f.write(json.dumps(venda) + "\n")
    print(f"Venda gerada: {venda}")
    time.sleep(2)
