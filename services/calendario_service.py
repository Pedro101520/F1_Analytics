import requests
import streamlit as st

from datetime import datetime
from models.calendario_model import Calendario

@st.cache_data
def rodadas():
    calendario = requests.get("https://api.jolpi.ca/ergast//f1/2026.json").json()
    acesso = calendario["MRData"]["RaceTable"]["Races"]

    total_rodadas = acesso[-1]["round"]
    
    data_atual = datetime.today()

    rodada_atual = None
    for i in acesso:
        data = datetime.strptime(i["date"], "%Y-%m-%d")

        rodada_atual = i
        if data_atual.date() <= data.date():
            break
    
    return Calendario(total_rodadas, rodada_atual)