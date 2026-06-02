import requests
from datetime import datetime
from google.cloud import storage
from google.oauth2 import service_account
import streamlit as st
import os
import json

ano_atual = datetime.now().year
hoje = datetime.now().date()

def get_storage_client():
    if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        return storage.Client()
    
    credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
    return storage.Client(
        credentials=credentials,
        project=credentials.project_id
    )

def info_equipes():
    equipes = {}
    infos = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/constructors/").json()
    for i in infos["MRData"]["ConstructorTable"]["Constructors"]:
        equipe_individual = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/constructors/{i["constructorId"]}/constructorstandings/").json()
        id_piloto = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/constructors/{i["constructorId"]}/drivers/").json()
        standings_lists = equipe_individual["MRData"]["StandingsTable"]["StandingsLists"]
        if not standings_lists:
            continue

        valor = standings_lists[0]["ConstructorStandings"][0]
        if i["constructorId"] not in equipes:
            equipes[i["constructorId"]] = {
                "nome": i["name"],
                "posicao": valor["positionText"],
                "pontos": valor["points"],
                "vitorias": valor["wins"],
                "nacionalidade": valor["Constructor"]["nationality"],
                "piloto_id": []
            }
        
        lists_equipe_piloto = id_piloto["MRData"]["DriverTable"]["Drivers"]
        for j in lists_equipe_piloto:
            equipes[i["constructorId"]]["piloto_id"].append(j["driverId"])

    return equipes


def salva_gcs():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "clever-axe-457319-g8-833d2d4ab67f.json"

    client = get_storage_client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_equipes.json")

    blob.upload_from_string(
        json.dumps(info_equipes(), ensure_ascii=False, indent=2),
        content_type="application/json"
    )

salva_gcs()