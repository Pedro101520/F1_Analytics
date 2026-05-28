import requests
from datetime import datetime
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

def estatisticas():
    infos_pilotos = {}

    for i in nome_id["id"]:
        acesso = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/drivers/{i}/results/").json()
        aceso_info = acesso["MRData"]["RaceTable"]["Races"]
        for j in aceso_info:
            aniversario = datetime.strptime(j["Results"][0]["Driver"]["dateOfBirth"], "%Y-%m-%d").date()
            idade = hoje.year - aniversario.year
            if hoje.month <= aniversario.month and hoje.day < aniversario.day:
                idade -= 1

            if i not in infos_pilotos:
                infos_pilotos[i] = {
                    "nome": f"{j["Results"][0]["Driver"]["givenName"]}",
                    "sobrenome": f"{j["Results"][0]["Driver"]["familyName"]}",
                    "nacionalidade": j["Results"][0]["Driver"]["nationality"],
                    "idade": idade,
                    "estreia": estreia[i]["ano"],
                    "posicao": posicao[i]["posicao"],
                    "pontos": posicao[i]["pontos"],
                    "sigla": j["Results"][0]["Driver"]["code"],
                    "numero": j["Results"][0]["number"],
                    "equipe": j["Results"][0]["Constructor"]["name"],
                    "vitorias": 0,
                    "podios": 0,
                    "melhor_resultado": int(j["Results"][0]["position"]),
                    "abandonos": 0
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

