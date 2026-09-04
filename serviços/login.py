from core.salvar_carregar import carregar_arq

arquivo = carregar_arq("data/usuarios.json")
def login(cpf, senha):
  try:
    if cpf in arquivo:
      usuario = arquivo[cpf]
      if usuario["senha"] == senha:
        return True, "login bem sucedido"
      else:
        return False, "usuario ou senha inválida"
    else:
      return False, "usuario ou senha inválida"
  except Exception as e:
    return False, "Error na aplicaçao"
