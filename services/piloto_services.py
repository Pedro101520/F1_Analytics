import requests
import streamlit as st
from datetime import datetime
from models.piloto_models import Lider, Estatisticas
from services.calendario_service import rodadas
from google.cloud import storage
from google.oauth2 import service_account
from dotenv import load_dotenv
import json
import os

ano_atual = datetime.now().year
infos_rodada = rodadas()
total_rodadas = infos_rodada.total_rodadas
load_dotenv()

def get_storage_client():
    if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        return storage.Client()
    
    credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
    return storage.Client(
        credentials=credentials,
        project=credentials.project_id
    )

@st.cache_data(ttl="1h")
def piloto_lider():
    piloto = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/driverstandings/").json()
    acesso = piloto["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    return Lider(acesso[0])

@st.cache_data(ttl="1h")
def estatisticas_piloto(id_piloto):
    client = get_storage_client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_pilotos.json")

    conteudo = blob.download_as_text()
    dados = json.loads(conteudo)
    
    return Estatisticas(**dados[id_piloto])

@st.cache_data(ttl="1h")
def lista_id():
    client = get_storage_client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_pilotos.json")

    conteudo = blob.download_as_text()
    dados = json.loads(conteudo)
    
    lista_id_piloto = list(dados.keys())
    nome_pilotos = []
    for i in lista_id_piloto:
        nome_pilotos.append(f"{dados[i]["nome"]} {dados[i]["sobrenome"]}")
    
    return {
        "ids": lista_id_piloto,
        "nomes": nome_pilotos
    }

