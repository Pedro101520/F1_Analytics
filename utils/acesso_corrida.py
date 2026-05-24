import json

def corrida():
    with open("assets\corrida.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados
    