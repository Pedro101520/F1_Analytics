import streamlit as st
from models.calendario_model import Calendario
from google.cloud import storage
from google.oauth2 import service_account
from dotenv import load_dotenv
import json
import os

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
def rodadas():
    client = get_storage_client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_calendario.json")

    conteudo = blob.download_as_text()
    dados = json.loads(conteudo)
    
    return Calendario(dados)