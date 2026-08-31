from flask import Flask, render_template, request
from servicos.cadastrar import cadastrar
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro', methods=['GET'])
def carregar_cadastro():
    return render_template('cadastrar.html')

@app.route('/cadastro', methods=['POST'])
def processar_cadastro():
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    cidade = request.form.get("cidade")
    email = request.form.get("email")
    nascimento = request.form.get("nascimento")
    senha = request.form.get("senha")
    sucesso, mensagem = cadastrar(cpf, nome, email, cidade, nascimento, senha)
    if sucesso:
       return render_template('sucesso.html')
    else:
       return render_template("cadastrar.html", error=mensagem)
if __name__ == "__main__":
   app.run(debug=True)
  
