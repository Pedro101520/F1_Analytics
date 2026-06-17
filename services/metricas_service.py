import streamlit as st
from datetime import datetime
from models.metricas_model import Modelo_Metricas
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

@st.cache_resource(ttl=3600)
def info_metricas():
    client = get_storage_client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob1 = bucket.blob("metricas_com_quali.json")
    conteudo = blob1.download_as_text()
    com_quali = json.loads(conteudo)

    blob2 = bucket.blob("metricas_sem_quali.json")
    conteudo2 = blob2.download_as_text()
    sem_quali = json.loads(conteudo2)
    
    return Modelo_Metricas(com_quali, sem_quali)