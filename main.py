import imaplib
import smtplib
import email
from email.message import EmailMessage
from datetime import datetime
import pandas as pd
from config import *

def escolher_resposta(assunto):
    assunto = assunto.lower()
    if "currículo" in assunto:
        return "responses/rh.txt", "Recebemos seu currículo"
    elif "orçamento" in assunto:
        return "responses/comercial.txt", "Sobre sua solicitação"
    else:
        return "responses/padrao.txt", "Resposta automática"

def ler_resposta(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        return f.read()

mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL, PASSWORD)
mail.select("inbox")

status, mensagens = mail.search(None, "UNSEEN")
ids = mensagens[0].split()

smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
smtp.starttls()
smtp.login(EMAIL, PASSWORD)

log = []

for e_id in ids:
    _, dados = mail.fetch(e_id, "(RFC822)")
    msg = email.message_from_bytes(dados[0][1])

    assunto = msg["subject"]
    remetente = email.utils.parseaddr(msg["From"])[1]

    arquivo, assunto_resposta = escolher_resposta(assunto)
    corpo = ler_resposta(arquivo)

    resposta = EmailMessage()
    resposta["From"] = EMAIL
    resposta["To"] = remetente
    resposta["Subject"] = assunto_resposta
    resposta.set_content(corpo)

    smtp.send_message(resposta)
    mail.store(e_id, '+FLAGS', '\\Seen')

    log.append({
        "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "email": remetente,
        "assunto": assunto
    })

smtp.quit()
mail.logout()

df = pd.DataFrame(log)
df.to_csv("logs/email_log.csv", index=False)
