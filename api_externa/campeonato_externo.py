import requests
from datetime import datetime
from google.cloud import storage
from google.oauth2 import service_account
import json
import os
import streamlit as st

ano_atual = datetime.now().year

def get_storage_client():
    if os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
        return storage.Client()
    
    credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp_service_account"])
    return storage.Client(
        credentials=credentials,
        project=credentials.project_id
    )


def tabela_campeonato():
    tabela_camp = {
        "tabela_pilotos": [],
        "tabela_equipes": []
    }

    acesso = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/driverstandings/").json()
    info = acesso["MRData"]["StandingsTable"]["StandingsLists"][0]

    acesso_equipe = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/constructorstandings/").json()
    info_equipe = acesso_equipe["MRData"]["StandingsTable"]["StandingsLists"][0]

    for i in info["DriverStandings"]:  
        tabela_camp["tabela_pilotos"].append({
            "nome": f"{i["Driver"]["givenName"]} {i["Driver"]["familyName"]}",
            "equipe": i["Constructors"][0]["name"],
            "pais": i["Driver"]["nationality"],
            "vitorias": i["wins"],
            "pontos": i["points"]
        })
    
    for j in info_equipe["ConstructorStandings"]:
        tabela_camp["tabela_equipes"].append({
            "nome": j["Constructor"]["name"],
            "pais": j["Constructor"]["nationality"],
            "vitorias": j["wins"],
            "pontos": j["points"]
        })

    return tabela_camp


def salva_gcs():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "clever-axe-457319-g8-833d2d4ab67f.json"

    client = get_storage_client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_campeonato.json")

    blob.upload_from_string(
        json.dumps(tabela_campeonato(), ensure_ascii=False, indent=2),
        content_type="application/json"
    )

salva_gcs()