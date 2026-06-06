import requests
import streamlit as st
from models.resultados_model import InfoUltimaCorrida
from services.calendario_service import rodadas
from datetime import datetime

rodada_atual = rodadas()

@st.cache_data(ttl="1h")
def resultados_corrida():
    ano_atual = datetime.now().year
    piloto = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/{rodada_atual.round}/results/").json()
    acesso = piloto["MRData"]["RaceTable"]["Races"][0]

    return InfoUltimaCorrida(acesso)
