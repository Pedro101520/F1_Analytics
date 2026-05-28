class Lider:
    def __init__(self, lider):
        nome_piloto = (f"{lider["Driver"]["givenName"]} {lider["Driver"]["familyName"]}")
        self.lider = nome_piloto
        self.pontos = lider["points"]

class Estatisticas:
    def __init__(self, nome, sobrenome, nacionalidade, idade, numero, equipe, vitorias, podio, melhor_resultado, abandonos, estreia, mundial):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nacionalidade = nacionalidade
        self.idade = idade
        self.numero = numero
        self.equipe = equipe
        self.vitorias = vitorias
        self.podio = podio
        self.melhor_resultado = melhor_resultado
        self.abandonos = abandonos
        self.estreia = estreia
        self.mundial = mundial