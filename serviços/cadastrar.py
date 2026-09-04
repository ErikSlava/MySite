from core.salvar_carregar import carregar_arq, salvar_dados

arquivos = carregar_arq("data/usuarios.json")
def cadastrar(cpf, nome, email, cidade, nascimento, senha):
    try:
       for usuario in arquivos:
          if usuario["cpf"] == cpf:
             return False, "cpf ja cadastrado"
          if usuario["email"]  == email:
             return False, "email ja cadastrado"

       novo_usuario = {
            cpf: {
                "cpf": cpf,
                "nome": nome,
                "email": email,
                "cidade": cidade,
                "tipo": "usuario",
                "saldo": 1000,
                "nascimento": nascimento,
                "senha": senha,
                "ativo": True
            }
        }
       arquivos.update(novo_usuario)
       salvar_dados(arquivos)
       return True, "usuario cadastrado com sucesso"

    except Exception as e:
      return False, f"erro na aplicaçao {e}"








