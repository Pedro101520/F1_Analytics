import streamlit as st
from datetime import datetime
from models.campeonato_model import Campeonato
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

@st.cache_data
def info_campeonato():
    client = get_storage_client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_campeonato.json")

    conteudo = blob.download_as_text()
    dados = json.loads(conteudo)
    
    return Campeonato(**dados)