import json

def carregar_arq(caminho):
  with open(f"{caminho}", "r") as arq:
    dados = json.load(arq)
  return dados

def slavar_dados(caminho, dados):
  with open(f"{caminho}", "w") as arq:
    json.dump(dados, arq, indent=4)
  return True
  
