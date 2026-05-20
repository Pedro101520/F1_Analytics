from datetime import datetime

class Calendario:
    def __init__(self, total_rodadas, rodada_atual):
        self.total_rodadas = total_rodadas
        self.round = int(rodada_atual["round"]) - 1
        self.circuito = rodada_atual["raceName"]

        data_hoje = datetime.now().date()
        data = datetime.strptime(rodada_atual["date"], "%Y-%m-%d").date()
        self.prox_corrida = (data - data_hoje).days