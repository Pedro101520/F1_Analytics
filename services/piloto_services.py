import requests
import streamlit as st
from datetime import datetime
from models.piloto_models import Lider

# @st.cache_data
def piloto_lider():
    ano_atual = datetime.now().year
    piloto = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/driverstandings/").json()
    acesso = piloto["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

    return Lider(acesso[0])
