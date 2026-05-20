class Lider:
    def __init__(self, lider):
        nome_piloto = (f"{lider["Driver"]["givenName"]} {lider["Driver"]["familyName"]}")
        self.lider = nome_piloto
        self.pontos = lider["points"]