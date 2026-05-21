import requests
import streamlit as st
from models.resultados_model import InfoUltimaCorrida
from services.calendario_service import rodadas

rodada_atual = rodadas()

# @st.cache_data
def resultados_corrida():
    piloto = requests.get(f"https://api.jolpi.ca/ergast/f1/2026/{rodada_atual.round}/results/").json()
    acesso = piloto["MRData"]["RaceTable"]["Races"][0]

    return InfoUltimaCorrida(acesso)
