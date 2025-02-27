from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ramirex9@gmail.com'  # Seu e-mail
app.config['MAIL_PASSWORD'] = 'dosw kveq qxlv aelt'  # Sua senha de app
app.config['MAIL_DEFAULT_SENDER'] = 'ramirex9@gmail.com'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Enviar para dois e-mails
        msg = Message(f'Novo contato de {name}', recipients=['ramirex9@gmail.com', 'ramirohd@gmail.com'])
        msg.body = f'Nome: {name}\nEmail: {email}\nTelefone: {phone}\nMensagem: {message}'

        # Enviar o e-mail
        mail.send(msg)

        # Redireciona para a página de sucesso após enviar
        return render_template('success.html')  

    except Exception as e:
        return f'Erro ao enviar mensagem: {e}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
