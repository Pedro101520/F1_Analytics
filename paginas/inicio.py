import streamlit as st
from services.calendario_service import rodadas
from services.piloto_services import piloto_lider
from services.resultados_service import resultados_corrida
from services.clima_service import clima
from utils.scraping.noticias import noticiaF1
from utils.acesso_circuito import circuito
from utils.acesso_corrida import corrida
import os
import base64

infos_rodada = rodadas()
infos_lider = piloto_lider()
infos_results = resultados_corrida()

total_rodadas = infos_rodada.total_rodadas
rodada_atual = infos_rodada.round
prox_circuito = infos_rodada.circuito
prox_corrida = infos_rodada.prox_corrida
proxima_cidade = infos_rodada.localidade
prox_data = infos_rodada.prox_corrida_data
circuitoId = infos_rodada.circuit_id
proximas_corridas = infos_rodada.prox_corrida_calendario

lider_atual = infos_lider.lider
pontuacao_lider = infos_lider.pontos

ultimo_circuito = infos_results.ultima_pista
ultimo_ganhador = infos_results.vitoria

try:
    info_clima = clima()
    temperatura = round(info_clima.temperatura)
    umidade = info_clima.umidade
    vento = info_clima.vento
    chuva = info_clima.chuva
    clima_code = info_clima.clima_texto
    raio_uv = info_clima.uv
except:
    temperatura = None
    umidade = None
    vento = None
    chuva = None
    clima_code = None
    raio_uv = None

def pagina_inicial():
    col1, col2, col3, col4 = st.columns(4)

    st.markdown("""
        <style>
            .metric-card {
                min-height: 110px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }
        </style>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    corridas_restantes = int(total_rodadas) - int(rodada_atual)
    with col1:
        st.container(border=True).markdown(
            f"""
                <div class='metric-card'>
                    <div>
                        <p style='margin:0; font-size:20px; font-weight:bold;'>Progresso da Temporada:</p>
                        <p style='margin:4px 0 0 0; color:#990012; font-size:26px; font-weight:bold;'>{corridas_restantes} <span style='font-size:16px; color:gray; font-weight:normal;'>corridas restantes</span></p>
                    </div>
                    <div style='display:flex; justify-content:space-between;'>
                        <p style='margin:0; font-size:16px; margin-bottom: 25px;'>Round {rodada_atual+1}/{total_rodadas}</p>
                        <p style='margin:0; font-size:16px; color:gray; margin-bottom: 25px;'>{rodada_atual} GPs concluídos</p>
                    </div>
            </div>
            """,
    unsafe_allow_html=True
        )

    with col2:
        st.container(border=True).markdown(
            f"""
            <div class='metric-card'>
                <div>
                    <p style='margin:0; font-size:20px; font-weight:bold;'>Líder do Campeonato:</p>
                    <p style='margin:4px 0 0 0; font-size:26px; font-weight:bold;'>{lider_atual}</p>
                </div>
                <p style='margin:0; font-size:16px; color:gray; margin-bottom: 25px;'>{pontuacao_lider} pontos</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col3:
        st.container(border=True).markdown(
            f"""
            <div class='metric-card'>
                <div>
                    <p style='margin:0; font-size:20px; font-weight:bold;'>Próxima Corrida:</p>
                    <p style='margin:4px 0 0 0; color:#990012; font-size:26px; font-weight:bold;'>{prox_circuito}</p>
                </div>
                <p style='margin:0; font-size:16px; color:gray; margin-bottom: 25px;'>Em {prox_corrida} dias</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col4:
        st.container(border=True).markdown(
            f"""
            <div class='metric-card'>
                <div>
                    <p style='margin:0; font-size:20px; font-weight:bold;'>Última Vitória:</p>
                    <p style='margin:4px 0 0 0; font-size:26px; font-weight:bold;'>{ultimo_ganhador}</p>
                </div>
                <p style='margin:0; font-size:16px; color:gray; margin-bottom: 25px;'>{ultimo_circuito}</p>
            </div>
            """, unsafe_allow_html=True
        )

    col5, col6= st.columns(2)
    with col5:
        with st.container(border=True, height=400):
            if temperatura != None:
                st.html(
                    f"""
                    <div style='padding: 4px 0 12px; gap: 30px'>

                        <div style='display: flex; align-items: center; gap: 8px; margin-bottom: 16px;'>
                            <span style='font-size: 20px; font-weight: 600;'>Previsão do Tempo —</span>
                            <span style='font-size: 20px; color: #aaa;'>{prox_circuito} · {proxima_cidade}</span>
                        </div>

                        <div style='display: flex; align-items: center; gap: 14px; margin-bottom: 16px;'>
                            <h2 style='font-size: 48px; margin: 0; padding: 0; font-weight: 700;'>{temperatura}°C</h2>
                            <div>
                                <p style='margin: 0; font-size: 18px; font-weight: 600;'>{clima_code}</p>
                                <p style='margin: 4px 0 0; font-size: 13px; color: #aaa;'>{prox_data} · dia da corrida</p>
                            </div>
                        </div>

                        <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 40px'>
                            <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                                <p style='margin: 0; font-size: 16px; color: #888;'>Chuva</p>
                                <p style='margin: 4px 0 0; font-size: 18px; font-weight: 700;'>{chuva}%</p>
                            </div>
                            <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                                <p style='margin: 0; font-size: 12px; color: #888;'>Vento</p>
                                <p style='margin: 4px 0 0; font-size: 18px; font-weight: 700;'>{vento} km/h</p>
                            </div>
                            <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                                <p style='margin: 0; font-size: 12px; color: #888;'>Umidade</p>
                                <p style='margin: 4px 0 0; font-size: 18px; font-weight: 700;'>{umidade}%</p>
                            </div>
                            <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                                <p style='margin: 0; font-size: 12px; color: #888;'>Raios UV</p>
                                <p style='margin: 4px 0 0; font-size: 18px; font-weight: 700;'>{raio_uv}</p>
                            </div>
                        </div>
                    </div>
                    """
                )
            else:
                st.write("## API de clima fora do ar, volte mais tarde para mais informações climáticas")
    with col6:
        container = st.container(border=True, height=400)
        container.markdown(
            f"""
                <h4 style='margin: -20px; padding:20px; font-size: 20px'>Últimas Notícias:</h4>
            """,
            unsafe_allow_html=True
        )
        for titulo, hora, link in zip(noticiaF1()["titulos"], noticiaF1()["hora"], noticiaF1()["links"]):
            container.write(titulo)
            container.caption(f"{hora} atrás")
            container.link_button("Ler Notícia", link, use_container_width=True)
            container.divider()
        
    col7, col8= st.columns(2)
    with col7:    
        container = st.container(border=True, height=450)

        with container:
            text_col, img_col = st.columns([3, 2])

            with text_col:
                st.markdown(
                    f"""
                        <div style='display: flex; align-items: center; gap: 8px; margin-bottom: 16px;'>
                            <span style='font-size: 20px; font-weight: 600;'>Próxima Corrida —</span>
                            <span style='font-size: 20px; color: #aaa;'>{circuito()[circuitoId][1]}</span>
                        </div>

                        <div style='align-items: center; gap: 8px; margin-bottom: 16px;'>
                            <p style='margin: 4px 0 0; font-size: 13px; color: #aaa;'>País</p>
                            <p style='margin: 0; font-size: 18px; font-weight: 600;'>{circuito()[circuitoId][0]} - {proxima_cidade}</p>
                        </div>
                        <div style='align-items: center; gap: 8px; margin-bottom: 16px;'>
                            <p style='margin: 4px 0 0; font-size: 13px; color: #aaa;'>Extensão da Volta</p>
                            <p style='margin: 0; font-size: 18px; font-weight: 600;'>{circuito()[circuitoId][2]}Km</p>
                        </div>
                        <div style='align-items: center; gap: 8px; margin-bottom: 16px;'>
                            <p style='margin: 4px 0 0; font-size: 13px; color: #aaa;'>Número de Voltas</p>
                            <p style='margin: 0; font-size: 18px; font-weight: 600;'>{circuito()[circuitoId][4]}</p>
                        </div>
                        <div style='align-items: center; gap: 8px; margin-bottom: 16px;'>
                            <p style='margin: 4px 0 0; font-size: 13px; color: #aaa;'>Tipo de Pista</p>
                            <p style='margin: 0; font-size: 18px; font-weight: 600;'>{circuito()[circuitoId][5]}</p>
                        </div>
                        <div style='align-items: center; gap: 8px; margin-bottom: 16px;'>
                            <p style='margin: 4px 0 0; font-size: 13px; color: #aaa;'>Recorde da Volta</p>
                            <p style='margin: 0; font-size: 18px; font-weight: 600;'>{circuito()[circuitoId][3]}</p>
                        </div>
                    """,
                    unsafe_allow_html=True
                )          
            with img_col:
                with img_col:
                    try:
                        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                        caminho = os.path.join(BASE_DIR, "..", "assets", "pistas", f"{circuito()[circuitoId][1]}.png")
                        with open(caminho, "rb") as f:
                            img_b64 = base64.b64encode(f.read()).decode()
                        st.markdown(
                            f"""
                            <div style='display: flex; align-items: center; justify-content: center; height: 100%; padding-top: 70px; margin-left: -90px;'>
                                <img src="data:image/png;base64,{img_b64}" width="280"/>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    except:
                        pass

    with col8:
        container = st.container(border=True, height=450)
        with container:
            
            linhas_html = f"""
                <tr>
                    <td style='color:#990012; font-weight:bold;'>{proximas_corridas["datas"][0]}</td>
                    <td style='color:#990012; font-weight:bold;'>{circuito()[proximas_corridas["premio"][0]][0]}</td>
                    <td style='color:#990012; font-weight:bold;'>{corrida()[proximas_corridas["premio"][0]]}</td>
                    <td style='color:#990012; font-weight:bold;'>{proximas_corridas["cidade"][0]}</td>
                </tr>
            """
            for data, premio, cidade in zip(proximas_corridas["datas"][1:], proximas_corridas["premio"][1:], proximas_corridas["cidade"][1:]):
                pais_nome = circuito()[premio][0]
                corrida_nome = corrida()[premio]
                linhas_html += f"""
                    <tr>
                        <td>{data}</td>
                        <td>{pais_nome}</td>
                        <td>{corrida_nome}</td>
                        <td>{cidade}</td>
                    </tr>
                """

            tabela_html = f"""
                <style>
                    .f1-table {{
                        width: 100%;
                        border-collapse: collapse;
                        font-family: sans-serif;
                        font-size: 14px;
                    }}
                    .f1-table td {{
                        padding: 8px 12px;
                        border-bottom: 1px solid #2a2a2a;
                        color: #e0e0e0;
                    }}
                    .f1-table tr:hover td {{
                        background-color: #1e1e1e;
                    }}
                    .f1-table td:first-child {{
                        color: #888;
                        white-space: nowrap;
                    }}
                    .f1-table td:last-child {{
                        color: #ffffff;
                        font-weight: 500;
                    }}
                </style>
                <table class="f1-table">
                    {linhas_html}
                </table>
            """
            st.html(f"""
                <div style='display: flex; align-items: center; gap: 8px; margin-bottom: 16px;'>
                    <span style='font-size: 20px; font-weight: 600;'>Próximas Corridas:</span>
                </div>
            """)              
            st.html(tabela_html)