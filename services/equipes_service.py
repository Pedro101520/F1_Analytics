import streamlit as st
import os
import json

from google.cloud import storage
from models.equipes_model import Equipes
from dotenv import load_dotenv

load_dotenv()

@st.cache_data
def estatisticas_equipe(id_equipe):
    client = storage.Client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_equipes.json")

    conteudo = blob.download_as_text()
    dados = json.loads(conteudo)
    
    return Equipes(**dados[id_equipe])

@st.cache_data
def lista_id_equipe():
    client = storage.Client()
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
