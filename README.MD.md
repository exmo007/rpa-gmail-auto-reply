# RPA – Resposta Automática de E-mails (Gmail)

Projeto simples de RPA em Python que automatiza a leitura de e-mails não lidos no Gmail e envia respostas automáticas com base em palavras-chave no assunto.

## Objetivo
Reduzir trabalho manual no atendimento por e-mail, garantindo respostas rápidas e padronizadas.

## Funcionalidades
- Leitura de e-mails não lidos
- Classificação por palavras-chave
- Envio automático de respostas
- Registro das ações em log (CSV)

## Tecnologias
- Python 3
- imaplib
- smtplib
- email
- pandas

## Estrutura do projeto
rpa-gmail-auto-reply/
├── main.py
├── config_example.py
├── responses/
├── logs/
└── README.md


## Configuração
1. Ative a verificação em duas etapas no Gmail
2. Gere uma **Senha de App**
3. Crie um arquivo `config.py` com base no `config_example.py`

## Execução
```bash
python main.py

Benefícios:
Economia de tempo
Padronização de respostas
Redução de erros humanos


