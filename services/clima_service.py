import requests
from models.clima_model import InfoClima

from services.calendario_service import rodadas

infos_rodada = rodadas()

def clima():
    consulta = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude=45.5006&longitude=-73.5228&daily=temperature_2m_max,precipitation_probability_max,wind_speed_10m_max,relative_humidity_2m_mean,weather_code,uv_index_max&forecast_days=16&timezone=auto").json()

    acesso = consulta["daily"]["time"]

    indice = 15
    for i, valor in enumerate(acesso):
        if (str(valor) == str(infos_rodada.prox_data)):
            indice = i
            break
    
    return InfoClima(consulta, indice)
