import subprocess
import time
import smtplib
from email.message import EmailMessage

INTERVALO = 60  # segundos (1 minuto)

def rodar_gerador():
    processo = subprocess.Popen(["python", "scripts/gerar_dados.py"])
    time.sleep(10)
    processo.terminate()

def transformar_dados():
    subprocess.run(["python", "scripts/transformar_dados.py"])

def exportar_sqlite():
    subprocess.run(["python", "scripts/exportar_sqlite.py"])

def enviar_alerta(subject, body):
    # Configurações do seu email
    EMAIL_REMETENTE = "seuemail@gmail.com"
    SENHA = "sua_senha_de_app"
    EMAIL_DESTINO = "destino@email.com"

    msg = EmailMessage()
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = EMAIL_DESTINO
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_REMETENTE, SENHA)
            smtp.send_message(msg)
        print("✅ Alerta enviado por email.")
    except Exception as e:
        print(f"❌ Falha ao enviar email: {e}")

def checar_vendas():
    import pandas as pd
    df = pd.read_parquet("../dados/silver/vendas.parquet")
    vendas_ultimos_10 = df.tail(10)['valor'].sum()
    print(f"Vendas últimos 10 registros: R$ {vendas_ultimos_10:.2f}")
    # Se vendas muito baixas, enviar alerta
    if vendas_ultimos_10 < 1000:  # ajuste o valor conforme sua regra
        enviar_alerta(
            "Alerta: Queda nas Vendas!",
            f"As vendas nos últimos 10 registros foram apenas R$ {vendas_ultimos_10:.2f}."
        )

if __name__ == "__main__":
    print("🚀 Pipeline contínuo iniciado. Ctrl+C para parar.")
    while True:
        rodar_gerador()
        transformar_dados()
        exportar_sqlite()
        checar_vendas()
        print(f"⏳ Aguardando {INTERVALO} segundos para próxima execução...\n")
        time.sleep(INTERVALO)
