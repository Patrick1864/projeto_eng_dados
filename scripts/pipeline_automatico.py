import subprocess
import time
import os

def rodar_gerador():
    print("🚀 Iniciando geração de dados...")
    processo = subprocess.Popen(["python", "scripts/gerar_dados.py"])
    time.sleep(10)  # gera por 10 segundos
    processo.terminate()
    print("✅ Dados gerados.")

def transformar_dados():
    print("⚙️ Processando dados...")
    subprocess.run(["python", "scripts/transformar_dados.py"])
    print("✅ Dados transformados.")

def exportar_sqlite():
    print("💾 Exportando para SQLite...")
    subprocess.run(["python", "scripts/exportar_sqlite.py"])
    print("✅ Exportação concluída.")

if __name__ == "__main__":
    rodar_gerador()
    transformar_dados()
    exportar_sqlite()
    print("🎉 Pipeline completo finalizado!")
