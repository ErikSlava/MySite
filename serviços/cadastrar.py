from core.salvar_carregar import carregar_arq, salvar_dados

arquivo = carregar_arq("../data/usuarios.json")
def validar(cpf, nome, email, cidade, nascimento, senha):
    try:
       for usuario in arquivos:
          if usuario["cpf"] == cpf:
             return False, "cpf ja cadastrado"
          if usuario["email"]  == email:
             return False, "email ja cadastrado"

       novo_usuario["cpf] = {
           "cpf": cpf,
           "nome": nome,
           "email": email,
           "cidade": cidade,
           "nascimento": nascimento,
           "senha": senha
        }
       salvar_dados(novo_usuario)
       return True, "usuario cadastrado com sucesso"

    except Exception as e:
      return False, f"erro na aplicaçao {e}"
