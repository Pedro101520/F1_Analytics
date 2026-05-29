class Lider:
    def __init__(self, lider):
        nome_piloto = (f"{lider["Driver"]["givenName"]} {lider["Driver"]["familyName"]}")
        self.lider = nome_piloto
        self.pontos = lider["points"]

class Estatisticas:
    def __init__(self, nome, sobrenome, nacionalidade, idade, estreia, posicao, media_largada, pontos, pole_position, sigla, numero, equipe, vitorias, podios, qtde_mundial, melhor_resultado, abandonos):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nacionalidade = nacionalidade
        self.idade = idade
        self.numero = numero
        self.equipe = equipe
        self.vitorias = vitorias
        self.podios = podios
        self.pole_positions = pole_position
        self.qtde_mundial = qtde_mundial
        self.melhor_resultado = melhor_resultado
        self.abandonos = abandonos
        self.estreia = estreia
        self.posicao = posicao
        self.media_largada = media_largada
        self.sigla = sigla
        self.pontos = pontos