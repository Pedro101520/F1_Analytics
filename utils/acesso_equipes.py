import json
import os

def leitura_equipe():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(BASE_DIR, "..", "assets", "equipes.json")
    with open(caminho, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados
