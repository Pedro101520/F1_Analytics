import requests
import streamlit as st
from datetime import datetime
from models.piloto_models import Lider, Estatisticas
from services.calendario_service import rodadas

ano_atual = datetime.now().year

infos_rodada = rodadas()
total_rodadas = infos_rodada.total_rodadas

@st.cache_data
def piloto_lider():
    piloto = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/driverstandings/").json()
    acesso = piloto["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]

    return Lider(acesso[0])

@st.cache_data
def lista_id():
    ids = []
    nomes = []

    calendario = requests.get(f"https://api.jolpi.ca/ergast/f1/2026/drivers/").json()

    for i in calendario["MRData"]["DriverTable"]["Drivers"]:
        ids.append(i["driverId"])
        nomes.append(f"{i["givenName"]} {i["familyName"]}")

    return {
        "id": ids,
        "nome": nomes
    }

@st.cache_data
def inicio_f1(id_piloto):
    acesso = requests.get(f"https://api.jolpi.ca/ergast/f1/drivers/{str(id_piloto)}/results?limit=1&offset=0").json()
    ano = acesso["MRData"]["RaceTable"]["Races"][0]["season"]
    return ano

@st.cache_data
def calculo_mundial(id_piloto):
    estreia = int(inicio_f1(id_piloto))
    mundial = 0

    while int(estreia) <= int(ano_atual):
        calendario = requests.get(f"https://api.jolpi.ca/ergast/f1/{estreia}.json").json()
        acesso = calendario["MRData"]["RaceTable"]["Races"]

        if not acesso:
            estreia += 1
            continue

        total_rodadas = int(acesso[-1]["round"])

        piloto = requests.get(
            f"https://api.jolpi.ca/ergast/f1/{estreia}/drivers/{str(id_piloto)}/driverstandings/"
        ).json()

        standings_lists = piloto["MRData"]["StandingsTable"]["StandingsLists"]

        # Pula se não houver dados para esse piloto nesse ano
        if not standings_lists or not standings_lists[0]["DriverStandings"]:
            estreia += 1
            continue

        standings = standings_lists[0]
        driver_standing = standings["DriverStandings"][0]

        if (
            int(driver_standing["position"]) == 1
            and total_rodadas == int(standings["round"])
        ):
            mundial += 1

        estreia += 1

    return mundial


@st.cache_data
def estatisticas_piloto(id_piloto):
    estatisticas = {}
    num_rodadas = int(total_rodadas)
    rodadas = []

    for i in range(1, (num_rodadas + 1)):
        piloto = requests.get(f"https://api.jolpi.ca/ergast/f1/{ano_atual}/{i}/results/?limit=1000").json()
        rodadas.append(piloto["MRData"]["RaceTable"]["Races"])


    for rodada in rodadas:
        for i in rodada:
            for piloto in i["Results"]:
                if piloto["Driver"]["driverId"] not in estatisticas:
                    hoje = datetime.now().date()
                    aniversario = datetime.strptime(piloto["Driver"]["dateOfBirth"], "%Y-%m-%d").date()

                    idade = hoje.year - aniversario.year

                    if hoje.month <= aniversario.month and hoje.day < aniversario.day:
                        idade -= 1

                    estatisticas[piloto["Driver"]["driverId"]] = {
                        "nome": piloto["Driver"]["givenName"],
                        "sobrenome": piloto["Driver"]["familyName"],
                        "nacionalidade": piloto["Driver"]["nationality"],
                        "idade": idade,
                        "numero": piloto["Driver"]["permanentNumber"],
                        "equipe": piloto["Constructor"]["name"],
                        "vitorias": 0,
                        "podio": 0,
                        "melhor_resultado": int(piloto["position"]),
                        "abandonos": 0,
                        "estreia": int(inicio_f1(id_piloto)),
                        "mundial": int(calculo_mundial(id_piloto))
                    }
                
                if int(piloto["position"]) == 1:
                    estatisticas[piloto["Driver"]["driverId"]]["vitorias"] += 1
                
                if int(piloto["position"]) <= 3:
                    estatisticas[piloto["Driver"]["driverId"]]["podio"] += 1
                
                if int(piloto["position"]) < estatisticas[piloto["Driver"]["driverId"]]["melhor_resultado"]:
                    estatisticas[piloto["Driver"]["driverId"]]["melhor_resultado"] = int(piloto["position"])
                
                if piloto["positionText"] == 'R':
                    estatisticas[piloto["Driver"]["driverId"]]["abandonos"] += 1
    
    return Estatisticas(**estatisticas[id_piloto])
