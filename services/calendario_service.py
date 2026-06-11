import requests
import streamlit as st

from datetime import datetime
from models.calendario_model import Calendario

@st.cache_data(ttl=3600)
def rodadas():
    ano_atual = datetime.now().year
    calendario = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}.json").json()
    acesso = calendario["MRData"]["RaceTable"]["Races"]

    total_rodadas = acesso[-1]["round"]
    
    data_atual = datetime.today()

    rodada_atual = None

    consulta = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/results/?limit=500").json()
    races = consulta["MRData"]["RaceTable"]["Races"]
    rodada = int(races[-1]["round"]) + 1
    rodada_atual = acesso[rodada]

    prox_corrida_calendario = []
    prox_grandes_premios = []
    prox_cidade = []
    for i in acesso:
        data = datetime.strptime(i["date"], "%Y-%m-%d")

        if data.date() >= data_atual.date(): 
            prox_corrida_calendario.append(i["date"])
            prox_cidade.append(i["Circuit"]["Location"]["locality"])
            prox_grandes_premios.append(i["raceName"])
    
    infos_corridas = {
        "datas": prox_corrida_calendario,
        "premio": prox_grandes_premios,
        "cidade": prox_cidade
    }

    return Calendario(total_rodadas, rodada_atual, infos_corridas)
