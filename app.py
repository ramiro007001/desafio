from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configuração do servidor SMTP do Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = "ramirex9@gmail.com"
app.config['MAIL_PASSWORD'] = "dosw kveq qxlv aelt"  # Use a senha gerada no passo 2

mail = Mail(app)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/send', methods=['POST'])
def send_email():
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    recado = request.form.get('recado')

    try:
        msg = Message("Novo contato do formulário",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=["ramirex9@gmail.com"])  # E-mail que vai receber

        msg.body = f"""
        Nome: {nome}
        Email: {email}
        Telefone: {telefone}
        Recado: {recado}
        """

        mail.send(msg)
        return "E-mail enviado com sucesso!"

    except Exception as e:
        return f"Erro ao enviar mensagem: {e}"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
