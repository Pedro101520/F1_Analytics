import requests
import streamlit as st
from datetime import datetime
from models.piloto_models import Lider, Estatisticas
from services.calendario_service import rodadas
from google.cloud import storage
import json
import os

ano_atual = datetime.now().year
infos_rodada = rodadas()
total_rodadas = infos_rodada.total_rodadas

@st.cache_data
def piloto_lider():
    piloto = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/driverstandings/").json()
    acesso = piloto["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    return Lider(acesso[0])

@st.cache_data
def estatisticas_piloto(id_piloto):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "clever-axe-457319-g8-833d2d4ab67f.json"

    client = storage.Client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_pilotos.json")

    conteudo = blob.download_as_text()
    dados = json.loads(conteudo)
    
    return Estatisticas(**dados[id_piloto])

@st.cache_data
def lista_id():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "clever-axe-457319-g8-833d2d4ab67f.json"

    client = storage.Client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_pilotos.json")

    conteudo = blob.download_as_text()
    dados = json.loads(conteudo)
    
    return list(dados.keys())

