usuarios = []
def validar(cpf, nome, email, cidade):
    try:
       for usuario in usuarios:
          if usuario["cpf"] == cpf:
             return False, "cpf ja cadastrado"
          if usuario["email"]  == email:
             return False, "email ja cadastrado"

       novo_usuario = {
           "cpf": cpf,
           "nome": nome,
           "email": email,
           "cidade": cidade
       }
       usuarios.append(novo_usuario)
       return True, "usuario cadastrado com sucesso"

    except Exception as e:
      return False, f"erro na aplicaçao {e}"
