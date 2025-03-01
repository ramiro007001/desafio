from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configurações do Flask-Mail para envio via Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ramirex9@gmail.com'  # Seu e-mail principal
app.config['MAIL_PASSWORD'] = 'dosw kveq qxlv aelt'  # Sua senha de app (senha de aplicativo gerada no Gmail)
app.config['MAIL_DEFAULT_SENDER'] = 'ramirex9@gmail.com'  # Pode ser o mesmo do username

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Coleta os dados do formulário
        nome = request.form['name']
        email = request.form['email']
        telefone = request.form['phone']
        mensagem = request.form['message']

        # Cria a mensagem a ser enviada
        msg = Message(f'Novo contato de {nome}', 
                      recipients=['ramirex9@gmail.com', 'ramirohd@gmail.com'])
        msg.body = f"Nome: {nome}\nEmail: {email}\nTelefone: {telefone}\nMensagem: {mensagem}"
        
        try:
            mail.send(msg)
            return redirect(url_for('success'))
        except Exception as e:
            return f"Erro ao enviar e-mail: {e}"
    return render_template('index.html')

@app.route('/success')
def success():
    return "Mensagem enviada com sucesso!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
