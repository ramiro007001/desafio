from flask import Flask, render_template, request
import mysql.connector
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configuração do banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ra@985235",
    database="seu_banco_de_dados"
)
cursor = db.cursor()

# Rota para exibir o formulário
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o formulário
@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    telefone = request.form['telefone']
    mensagem = request.form['mensagem']

    # 🔴 Inserindo dados no banco de dados
    sql = "INSERT INTO contatos (nome, email, telefone, mensagem) VALUES (%s, %s, %s, %s)"
    valores = (nome, email, telefone, mensagem)
    cursor.execute(sql, valores)
    db.commit()

    # 🔴 Enviando e-mail
    sender_email = "ramirex9@gmail.com"
    sender_password = "dosw kveq qxlv aelt"

    recipients = ["ramirex9@gmail.com", "ramirohd@gmail.com"]
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = "Novo Contato Recebido"
    corpo = f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nMensagem: {mensagem}"
    msg.attach(MIMEText(corpo, 'plain'))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipients, msg.as_string())
    server.quit()

    return "Mensagem enviada e salva com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
