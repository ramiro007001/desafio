import os
from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Página inicial com o formulário
@app.route('/')
def form():
    return render_template('form.html')

# Envio do formulário
@app.route('/send', methods=['POST'])
def send_email():
    # Obtenha os dados do formulário
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    # Configurações de envio de e-mail
    sender_email = "ramirex9@gmail.com"
    receiver_emails = ["ramirex9@gmail.com", "ramriohd@gmail.com"]  # Adicione os dois e-mails aqui
    password = "dosw kveq qxlv aelt"

    # Criando a mensagem
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_emails)
    msg['Subject'] = "Novo formulário enviado"
    body = f"Nome: {name}\nE-mail: {email}\nTelefone: {phone}\nMensagem: {message}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Envio do e-mail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_emails, text)
        
        return render_template('success.html')  # Página de sucesso após envio do formulário

    except Exception as e:
        return f"Erro ao enviar mensagem: {str(e)}"

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))  # Porta configurada para o Render
