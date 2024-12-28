from flask import Flask, render_template, request

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Página inicial (GET)
@app.route('/')
def home():
    return render_template('index.html')

# Página de submit (POST)
@app.route('/submit', methods=['POST'])
def submit():
    # Aqui você pode pegar os dados enviados pelo formulário
    name = request.form.get('name')
    email = request.form.get('email')
    # Processar ou armazenar esses dados conforme necessário
    return f"Nome: {name}, Email: {email}"

# Executar o aplicativo
if __name__ == "__main__":
    app.run(debug=True)

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')
