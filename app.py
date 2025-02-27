from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')  # Isso renderiza o seu form.html

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Certifique-se de que está rodando com o host '0.0.0.0' para funcionar no Render





from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'seuemail@gmail.com'  # Coloque seu e-mail
app.config['MAIL_PASSWORD'] = 'suasenha'  # Coloque sua senha
app.config['MAIL_DEFAULT_SENDER'] = 'seuemail@gmail.com'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    msg = Message(f'Novo contato de {name}', recipients=['ramirex9@gmail.com'])
    msg.body = f'Nome: {name}\nEmail: {email}\nTelefone: {phone}\nMensagem: {message}'

    try:
        mail.send(msg)
        return 'Mensagem enviada com sucesso!'
    except Exception as e:
        return f'Erro ao enviar mensagem: {e}'

if __name__ == '__main__':
    app.run(debug=True)