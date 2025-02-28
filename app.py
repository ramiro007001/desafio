from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Defina as credenciais e configurações do e-mail
EMAIL_SENDER = "ramirex9@gmail.com"
EMAIL_PASSWORD = "dosw kveq qxlv aelt"  # Insira aqui a senha do aplicativo do Gmail
EMAIL_RECEIVER = "ramirex9@gmail.com"  # Insira o primeiro e-mail
EMAIL_RECEIVER_2 = "ramirohd@gmai.com"  # Insira o segundo e-mail

# Rota para o formulário
@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Coleta os dados do formulário
        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        mensagem = request.form.get("mensagem")

        # Envia o email com os dados do formulário
        send_email(nome, email, telefone, mensagem)
        return redirect(url_for("success"))  # Redireciona para a página de sucesso
    return render_template("form.html")

# Rota para a página de sucesso
@app.route("/success")
def success():
    return render_template("success.html")  # Exibe a página de sucesso

# Função para enviar o email
def send_email(nome, email, telefone, mensagem):
    try:
        # Configuração do servidor SMTP do Gmail
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)

        # Preparando o e-mail
        subject = "Formulário de Contato - Novo Envio"
        body = f"""
        Nome: {nome}
        Email: {email}
        Telefone: {telefone}
        
        Mensagem:
        {mensagem}
        """

        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Envia o e-mail para o primeiro destinatário
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

        # Envia o e-mail para o segundo destinatário
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER_2, msg.as_string())

        # Fecha a conexão com o servidor
        server.quit()
    except Exception as e:
        return f'Erro ao enviar mensagem: {e}'

if __name__ == "__main__":
    app.run(debug=True)
