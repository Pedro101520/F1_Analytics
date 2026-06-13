import requests
from models.clima_model import InfoClima
import streamlit as st

from services.calendario_service import rodadas

infos_rodada = rodadas()

@st.cache_resource(ttl=3600)
def clima():
    latitute = (infos_rodada.lat)
    longetude = infos_rodada.long

    consulta = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitute}&longitude={longetude}&daily=temperature_2m_max,precipitation_probability_max,wind_speed_10m_max,relative_humidity_2m_mean,weather_code,uv_index_max&forecast_days=16&timezone=auto", timeout=5).json()

    acesso = consulta["daily"]["time"]

    indice = 15
    for i, valor in enumerate(acesso):
        if (str(valor) == str(infos_rodada.prox_data)):
            indice = i
            break
    
    return InfoClima(consulta, indice)
