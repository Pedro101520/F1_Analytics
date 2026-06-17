import requests
import os
import streamlit as st
import json

from datetime import datetime
from google.cloud import storage
from google.oauth2 import service_account

def get_storage_client():
    if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        return storage.Client()
    
    credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
    return storage.Client(
        credentials=credentials,
        project=credentials.project_id
    )

def rodadas():
    ano_atual = datetime.now().year
    calendario = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}.json").json()
    acesso = calendario["MRData"]["RaceTable"]["Races"]

    total_rodadas = acesso[-1]["round"]
    
    data_atual = datetime.today()

    rodada_atual = None

    consulta = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/results/?limit=500").json()
    races = consulta["MRData"]["RaceTable"]["Races"]
    rodada = int(races[-1]["round"]) + 1
    rodada_atual = acesso[rodada]

    prox_corrida_calendario = []
    prox_grandes_premios = []
    prox_cidade = []
    lat = []
    long = []
    for i in acesso:
        data = datetime.strptime(i["date"], "%Y-%m-%d")

        if data.date() >= data_atual.date(): 
            prox_corrida_calendario.append(i["date"])
            prox_cidade.append(i["Circuit"]["Location"]["locality"])
            prox_grandes_premios.append(i["raceName"])
            lat.append(i["Circuit"]["Location"]["lat"])
            long.append(i["Circuit"]["Location"]["long"])
    
    infos_corridas = {
        "datas": prox_corrida_calendario,
        "premio": prox_grandes_premios,
        "cidade": prox_cidade,
        "lat": lat,
        "long": long,
        "total_rodadas": total_rodadas,
        "rodada_atual": rodada_atual
    }

    return infos_corridas


def salva_gcs():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "clever-axe-457319-g8-833d2d4ab67f.json"

    client = get_storage_client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_calendario.json")

    blob.upload_from_string(
        json.dumps(rodadas(), ensure_ascii=False, indent=2),
        content_type="application/json"
    )

salva_gcs()