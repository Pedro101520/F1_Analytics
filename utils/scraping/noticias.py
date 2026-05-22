import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

url = "https://motorsport.uol.com.br/f1/news/"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/136.0.0.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers)
parsed_html = BeautifulSoup(response.text, "html.parser")

def noticiaF1():
    lista_titulos = []
    titulos = parsed_html.find_all('div', attrs={'class': 'ms-item__info'})
    for titulo in titulos:
        try:
            conteudo = titulo.find('div', attrs={'class': 'ms-item__title'}).get_text()
            lista_titulos.append(conteudo)

            if len(lista_titulos) == 10:
                break
        except:
            continue
    
    lista_horarios = []
    novo_fuso = pytz.timezone("America/Sao_Paulo")
    data_atual = datetime.now(novo_fuso)
    horarios = parsed_html.find_all('div', attrs={'class': 'ms-item__info-top'})
    for hora in horarios:
        conteudo = hora.find('time', attrs={'class': 'ms-item__date'})
        try:
            data = conteudo.get('datetime')

            data = datetime.strptime(data, "%Y-%m-%dT%H:%M:%SZ")
            data = pytz.utc.localize(data)
            data = data.astimezone(novo_fuso)

            diferenca = data_atual - data

            total_segundos = int(diferenca.total_seconds())
            horas = total_segundos // 3600
            minutos = (total_segundos % 3600) // 60
            if horas != 0:
                lista_horarios.append(f"{horas}h {minutos}min")
            else:
                lista_horarios.append(f"{minutos}min")

            if len(lista_horarios) == 10:
                break
        except:
            continue
    
    lista_links = []
    bloco = parsed_html.find('div', attrs={'class': 'ms-content__main ms-items-widget'})
    links = bloco.find_all('a')

    for link in links:
        link_filtrado = link.get('href')
        if "live" in link_filtrado:
            continue
        else:
            novo_link = f"https://motorsport.uol.com.br/{link_filtrado}"
            lista_links.append(novo_link)

        if len(lista_links) == 10:
            break

    return {
        "titulos": lista_titulos,
        "hora": lista_horarios,
        "links": lista_links
    }