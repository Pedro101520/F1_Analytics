import requests
from datetime import datetime
from google.cloud import storage
import os
import json

ano_atual = datetime.now().year
hoje = datetime.now().date()

def info_equipes():
    equipes = {}
    infos = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/constructors/").json()
    for i in infos["MRData"]["ConstructorTable"]["Constructors"]:
        if i["constructorId"] not in equipes:
            equipes[i["constructorId"]] = {
                "nome": i["name"]
            }


    return equipes


def salva_gcs():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "clever-axe-457319-g8-833d2d4ab67f.json"

    client = storage.Client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_equipes.json")

    blob.upload_from_string(
        json.dumps(info_equipes(), ensure_ascii=False, indent=2),
        content_type="application/json"
    )

salva_gcs()