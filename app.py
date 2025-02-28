from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

app = Flask(__name__)

# Função para validar o e-mail
def is_valid_email(email):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(email_regex, email)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/send', methods=['POST'])
def send_email():
    # Obtenha os dados do formulário
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')

    # Verificar se todos os campos foram preenchidos
    if not name or not email or not phone or not message:
        return "Todos os campos são obrigatórios!", 400

    # Verificar formato do e-mail
    if not is_valid_email(email):
        return "E-mail inválido!", 400

    # Configurações do servidor de e-mail
    sender_email = "ramirex9@gmail.com"
    sender_password = "dosw kveq qxlv aelt"
    receiver_email_1 = "ramirex9@gmail.com"
    receiver_email_2 = "ramirohd@gmai.com"
    # Preparando a mensagem
    subject = "Novo Formulário de Contato"
    body = f"Nome: {name}\nE-mail: {email}\nTelefone: {phone}\nMensagem: {message}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email_1
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    msg2 = MIMEMultipart()
    msg2['From'] = sender_email
    msg2['To'] = receiver_email_2
    msg2['Subject'] = subject
    msg2.attach(MIMEText(body, 'plain'))

    try:
        # Conectando ao servidor e enviando o e-mail
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, [receiver_email_1, receiver_email_2], msg.as_string())
        return redirect(url_for('success'))
    except Exception as e:
        return f"Erro ao enviar e-mail: {e}"

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
