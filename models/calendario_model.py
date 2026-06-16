from datetime import datetime
import json
import os

class Calendario:
    def __init__(self, total_rodadas, rodada_atual, prox_corrida_calendario):
        self.total_rodadas = total_rodadas
        self.round = int(rodada_atual["round"])
        print(self.round)


        data_hoje = datetime.now().date()
        data = datetime.strptime(prox_corrida_calendario["datas"][0], "%Y-%m-%d").date()

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(BASE_DIR, "..", "assets", "corrida.json")
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        # Data sem formatação
        self.prox_data = data

        self.prox_corrida_data = data.strftime("%d/%m/%Y")
        
        self.prox_corrida = (data - data_hoje).days

        self.circuit_id = prox_corrida_calendario["premio"][0]

        try:
            circuito_traduzido = dados[prox_corrida_calendario["premio"][0]]
        except:
            circuito_traduzido = prox_corrida_calendario["premio"][0]

        self.circuito = circuito_traduzido
        self.localidade = prox_corrida_calendario["cidade"][0]

        self.lat = prox_corrida_calendario["lat"][0]
        self.long = prox_corrida_calendario["long"][0]

        self.prox_corrida_calendario = prox_corrida_calendario