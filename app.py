from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/send', methods=['POST'])
def send_email():
    nome = request.form.get('nome')
    email = request.form.get('email')
    telefone = request.form.get('telefone')
    recado = request.form.get('recado')

    print(f"Nome: {nome}, Email: {email}, Telefone: {telefone}, Recado: {recado}")
    return "Formulário enviado com sucesso!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
