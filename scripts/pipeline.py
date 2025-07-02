import subprocess
import time
import os

# Caminhos
CAMINHO_GERADOR = "scripts/gerar_dados.py"
CAMINHO_TRANSFORMADOR = "scripts/transformar_dados.py"

# Passo 1: Rodar o gerador por 10 segundos
print("🔄 Iniciando geração de dados simulados...")
processo = subprocess.Popen(["python", CAMINHO_GERADOR])
time.sleep(10)  # Tempo para gerar dados
processo.terminate()
print("✅ Dados gerados.")

# Passo 2: Executar a transformação
print("⚙️  Processando dados com Pandas...")
subprocess.run(["python", CAMINHO_TRANSFORMADOR])
print("✅ Transformação concluída.")

# Passo 3: Abrir o dashboard (opcional)
abrir_dashboard = input("Deseja abrir o dashboard Streamlit agora? (s/n): ").lower()
if abrir_dashboard == "s":
    print("🚀 Abrindo dashboard...")
    os.system("streamlit run dashboard/dashboard_streamlit.py")
else:
    print("✅ Pipeline finalizado.")
