import json

class InfoUltimaCorrida:
    def __init__(self, corrida):
        nome = corrida["Results"][0]["Driver"]["givenName"]
        sobrenome = corrida["Results"][0]["Driver"]["familyName"]

        with open("assets\corrida.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        try:
            circuito_traduzido = dados[corrida["raceName"]]
        except:
            circuito_traduzido = corrida["raceName"]

        self.ultima_pista = circuito_traduzido
        self.vitoria = f"{nome} {sobrenome}"
