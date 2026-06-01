import requests
from datetime import datetime
from google.cloud import storage
import json
import os
import time

ano_atual = datetime.now().year
hoje = datetime.now().date()

def lista_id():
    ids = []
    infos = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/drivers/").json()
    for i in infos["MRData"]["DriverTable"]["Drivers"]:
        ids.append(i["driverId"])


    return {
        "id": ids
    }
nome_id = lista_id()

def inicio_f1():
    time.sleep(60)
    estreia = {}
    for i in nome_id["id"]:
        acesso = requests.get(f"https://api.jolpi.ca/ergast/f1/drivers/{i}/results/?limit=10&offset=0").json()
        try:
            if i not in estreia:
                estreia[i] = {
                    "ano": acesso["MRData"]["RaceTable"]["Races"][0]["season"]
                }
        except:
            if i not in estreia:
                estreia[i] = {
                    "ano": 0
                }
    return estreia
estreia = inicio_f1()

def posicao_campeonato():
    time.sleep(60)
    posicao = {}
    for i in nome_id["id"]:
        acesso = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/drivers/{i}/driverstandings/").json()
        try:
            if i not in posicao:
                posicao[i] = {
                    "posicao": acesso["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["position"],
                    "pontos": acesso["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["points"]
                }
        except:
            if i not in posicao:
                posicao[i] = {
                    "posicao": 0,
                    "pontos": 0
                }
    return posicao
posicao = posicao_campeonato()

def pole_position():
    time.sleep(60)
    pole = {}
    for i in nome_id["id"]:
        acesso = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/drivers/{i}/qualifying/1/").json()
        if i not in pole:
            pole[i] = {
                "qtde_pole_position": acesso["MRData"]["total"]
            }

    return pole
pole = pole_position()

def media_posicao():
    time.sleep(60)
    media = {}
    for i in nome_id["id"]:
        acesso = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/drivers/{i}/results/").json()
        if i not in media:
            media[i] = {
                "media": "N/A"
            }
        
        grid = 0
        total_valido = 0
        for j in acesso["MRData"]["RaceTable"]["Races"]:
            grid_posicao = int(j["Results"][0]["grid"])
            if grid_posicao > 0:
                grid += grid_posicao
                total_valido += 1
        
        if total_valido  > 0:
            media[i]["media"] = str(grid / total_valido)

    return media
largada = media_posicao()


def calculo_mundial():
    time.sleep(60)
    mundiais = {}

    lista_estreia = []
    for i in nome_id["id"]:
        lista_estreia.append(estreia[i]["ano"])

    if 0 in lista_estreia:
        lista_estreia.remove(0)
    menor_ano = min(lista_estreia)

    for i in nome_id["id"]:
        if i not in mundiais:
            mundiais[i] = {
                "qtde_mundial": 0
            }

    for i in range(int(menor_ano), int(ano_atual)):
        acesso = requests.get(f"https://api.jolpi.ca/ergast/f1/{i}/driverstandings/1.json").json()
        vencedor_mundial = acesso["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["Driver"]["driverId"]
        if vencedor_mundial in mundiais:
            mundiais[vencedor_mundial]["qtde_mundial"] += 1
    
    return mundiais

qtde_mundial = calculo_mundial()


def pontos_posicao():
    time.sleep(60)
    posicao_valor = []
    for i in nome_id["id"]:
        acesso = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/drivers/{i}/results/").json()
        acesso_sprint = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/drivers/{i}/sprint/").json()
        rodada = acesso["MRData"]["RaceTable"]["Races"]
        rodada_sprint = acesso_sprint["MRData"]["RaceTable"]["Races"]

        dicionario_sprint = {}
        for sprint in rodada_sprint:
            if sprint["round"] not in dicionario_sprint:
                dicionario_sprint[sprint["round"]] = sprint["SprintResults"][0]["points"]

        for j in rodada:
            posicao_valor.append({
                "id_piloto": j["Results"][0]["Driver"]["driverId"],
                "gp": j["Circuit"]["circuitName"],
                "round": j["round"],
                "ponto_por_corrida": j["Results"][0]["points"],
                "posicao": j["Results"][0]["positionText"],
                "pontos_sprint": dicionario_sprint.get(j["round"], "0"),
                "id_gp": j["raceName"]
            })
    return posicao_valor
info_por_corrida = pontos_posicao()

info_agrupada = {}
for i in info_por_corrida:
    if i["id_piloto"] not in info_agrupada:
        info_agrupada[i["id_piloto"]] = {
            "corridas": []
        }
    
    info_agrupada[i["id_piloto"]]["corridas"].append({
        "gp": i["gp"],
        "round": i["round"],
        "ponto_por_corrida": i["ponto_por_corrida"],
        "posicao": i["posicao"],
        "pontos_por_sprint": i["pontos_sprint"],
        "id_gp": i["id_gp"]
    })

def estatisticas():
    time.sleep(60)
    infos_pilotos = {}

    for i in nome_id["id"]:
        acesso = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/drivers/{i}/results/").json()
        aceso_info = acesso["MRData"]["RaceTable"]["Races"]
        for j in aceso_info:
            aniversario = datetime.strptime(j["Results"][0]["Driver"]["dateOfBirth"], "%Y-%m-%d").date()
            idade = hoje.year - aniversario.year
            if (hoje.month < aniversario.month) or (hoje.month == aniversario.month and aniversario.day >= hoje.day):
                idade -= 1

            if i not in infos_pilotos:
                infos_pilotos[i] = {
                    "nome": f"{j["Results"][0]["Driver"]["givenName"]}",
                    "sobrenome": f"{j["Results"][0]["Driver"]["familyName"]}",
                    "nacionalidade": j["Results"][0]["Driver"]["nationality"],
                    "idade": idade,
                    "estreia": estreia[i]["ano"],
                    "posicao": posicao[i]["posicao"],
                    "media_largada": largada[i]["media"],
                    "pontos": posicao[i]["pontos"],
                    "pole_position": pole[i]["qtde_pole_position"],
                    "sigla": j["Results"][0]["Driver"]["code"],
                    "numero": j["Results"][0]["number"],
                    "equipe": j["Results"][0]["Constructor"]["name"],
                    "vitorias": 0,
                    "podios": 0,
                    "qtde_mundial": qtde_mundial[i]["qtde_mundial"],
                    "melhor_resultado": int(j["Results"][0]["position"]),
                    "abandonos": 0,
                    "pontuacao_individual": info_agrupada[i]["corridas"]
                }

            if int(j["Results"][0]["position"]) == 1:
                infos_pilotos[i]["vitorias"] += 1
            
            if int(j["Results"][0]["position"]) <= 3:
                infos_pilotos[i]["podios"] += 1
            
            if infos_pilotos[i]["melhor_resultado"] > int(j["Results"][0]["position"]):
                infos_pilotos[i]["melhor_resultado"] = int(j["Results"][0]["position"])
            
            if j["Results"][0]["positionText"] == 'R':
                infos_pilotos[i]["abandonos"] += 1
                
    return infos_pilotos

def salva_gcs():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "clever-axe-457319-g8-833d2d4ab67f.json"

    client = storage.Client()
    bucket = client.bucket("f1-dashboard-pilotos")
    blob = bucket.blob("f1_pilotos.json")

    blob.upload_from_string(
        json.dumps(estatisticas(), ensure_ascii=False, indent=2),
        content_type="application/json"
    )

salva_gcs()