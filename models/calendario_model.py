from datetime import datetime
import json
import os

class Calendario:
    def __init__(self, total_rodadas, rodada_atual, prox_corrida_calendario):
        self.total_rodadas = total_rodadas
        self.round = int(rodada_atual["round"]) - 1


        data_hoje = datetime.now().date()
        data = datetime.strptime(rodada_atual["date"], "%Y-%m-%d").date()

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(BASE_DIR, "..", "assets", "corrida.json")
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        # Data sem formatação
        self.prox_data = data

        self.prox_corrida_data = data.strftime("%d/%m/%Y")
        
        self.prox_corrida = (data - data_hoje).days

        self.circuit_id = rodada_atual["raceName"]

        try:
            circuito_traduzido = dados[rodada_atual["raceName"]]
        except:
            circuito_traduzido = rodada_atual["raceName"]

        self.circuito = circuito_traduzido
        self.localidade = rodada_atual["Circuit"]["Location"]["locality"]

        self.lat = rodada_atual["Circuit"]["Location"]["lat"]
        self.long = rodada_atual["Circuit"]["Location"]["long"]

        self.prox_corrida_calendario = prox_corrida_calendario