import streamlit as st
import os
import json

from google.cloud import storage
from google.oauth2 import service_account
from models.equipes_model import Equipes
from dotenv import load_dotenv

load_dotenv()
def get_storage_client():
    if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        return storage.Client()

    credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
    return storage.Client(
        credentials=credentials,
        project=credentials.project_id
    )

@st.cache_data(ttl=3600)
def estatisticas_equipe(id_equipe):
    client = get_storage_client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_equipes.json")

    conteudo = blob.download_as_text()
    dados = json.loads(conteudo)
    
    return Equipes(**dados[id_equipe])

@st.cache_data(ttl=3600)
def lista_id_equipe():
    client = get_storage_client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_equipes.json")

    conteudo = blob.download_as_text()
    dados = json.loads(conteudo)

    lista_id_equipe = list(dados.keys())
    nome_equipe = []
    for i in lista_id_equipe:
        nome_equipe.append(f"{dados[i]["nome"]}")
    
    return {
        "ids": lista_id_equipe,
        "nomes": nome_equipe
    }
