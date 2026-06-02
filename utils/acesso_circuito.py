import json

def circuito():
    with open("assets/circuitos.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados
    