import requests
from datetime import datetime
import streamlit as st

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
    
    return {
        "total_rodadas": total_rodadas,
        "rodada_atual": rodada_atual
    }