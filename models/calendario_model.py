from datetime import datetime
import json
import os

class Calendario:
    def __init__(self, dados):
        self.total_rodadas = dados["total_rodadas"]
        self.round = int(dados["rodada_atual"]["round"])

        data_hoje = datetime.now().date()
        data = datetime.strptime(dados["datas"][0], "%Y-%m-%d").date()

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(BASE_DIR, "..", "assets", "corrida.json")
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados_json = json.load(arquivo)

        # Data sem formatação
        self.prox_data = data

        self.prox_corrida_data = data.strftime("%d/%m/%Y")
        
        self.prox_corrida = (data - data_hoje).days

        self.circuit_id = dados["premio"][0]

        try:
            circuito_traduzido = dados_json[dados["premio"][0]]
        except:
            circuito_traduzido = dados["premio"][0]

        self.circuito = circuito_traduzido
        self.localidade = dados["cidade"][0]

        self.lat = dados["lat"][0]
        self.long = dados["long"][0]

        self.prox_corrida_calendario = dados