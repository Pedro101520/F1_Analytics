class Lider:
    def __init__(self, lider):
        nome_piloto = (f"{lider["Driver"]["givenName"]} {lider["Driver"]["familyName"]}")
        self.lider = nome_piloto
        self.pontos = lider["points"]

class Estatisticas:
    def __init__(self, nome, sobrenome, nacionalidade, idade, estreia, posicao, pontos, sigla, numero, equipe, vitorias, podios, melhor_resultado, abandonos):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nacionalidade = nacionalidade
        self.idade = idade
        self.numero = numero
        self.equipe = equipe
        self.vitorias = vitorias
        self.podios = podios
        self.melhor_resultado = melhor_resultado
        self.abandonos = abandonos
        self.estreia = estreia
        self.posicao = posicao
        self.sigla = sigla
        self.pontos = pontos