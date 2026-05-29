from google.cloud import storage
import json
import os

def ler_gcs():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "clever-axe-457319-g8-833d2d4ab67f.json"

    client = storage.Client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_pilotos.json")

    conteudo = blob.download_as_text()
    dados = json.loads(conteudo)
    
    return dados

print(list(ler_gcs().keys()))