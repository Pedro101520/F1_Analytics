class InfoUltimaCorrida:
    def __init__(self, corrida):
        nome = corrida["Results"][0]["Driver"]["givenName"]
        sobrenome = corrida["Results"][0]["Driver"]["familyName"]
        self.ultima_pista = corrida["raceName"]
        self.vitoria = f"{nome} {sobrenome}"
