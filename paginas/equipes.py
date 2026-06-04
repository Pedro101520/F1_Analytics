import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

from services.equipes_service import lista_id_equipe, estatisticas_equipe
from services.piloto_services import estatisticas_piloto
from utils.acesso_equipes import leitura_equipe
from utils.acesso_corrida import corrida

ano_atual = datetime.now().year

def info_pilotos(infos_estatisticas):
    lista_pilotos = []
    for i in infos_estatisticas.piloto_id:
        try:
            lista_pilotos.append(estatisticas_piloto(i))
        except:
            continue
    
    pilotos = {
        "vitorias": 0,
        "podios": 0,
        "pole_positions": 0,
        "melhor_resultado": 100,
        "abandonos": 0,
        "media_largada": "0"
    }
    soma = 0
    for i in lista_pilotos:
        pilotos["vitorias"] += i.vitorias
        pilotos["podios"] += i.podios
        pilotos["pole_positions"] += i.pole_positions

        if i.melhor_resultado < pilotos["melhor_resultado"]:
            pilotos["melhor_resultado"] = i.melhor_resultado
        
        pilotos["abandonos"] += i.abandonos

        soma += float(i.media_largada)
    try:
        pilotos["media_largada"] = f"{soma/len(lista_pilotos):.1f}"
    except ZeroDivisionError:
        pilotos["media_largada"] = 0

    return pilotos


def calculo_diferenca(info1, info2, inverte):
    valor1 = float(info1)
    valor2 = float(info2)

    if inverte == False:
        if valor1 < valor2:
            return {
                "html": "color:green",
                "diferenca": f"▲ {abs(valor1 - valor2):.1f}"
            }
        elif valor1 > valor2:
            return {
                "html": "color:red",
                "diferenca": f"▼ {(valor1 - valor2):.1f}"
            }
        elif valor1 == valor2:
            return {
                "html": "color:yellow",
                "diferenca": "▬"
            }
    else:
        if valor1 > valor2:
            return {
                "html": "color:green",
                "diferenca": f"▲ {abs(valor1 - valor2):.1f}"
            }
        elif valor1 < valor2:
            return {
                "html": "color:red",
                "diferenca": f"▼ {abs(valor1 - valor2):.1f}"
            }
        elif valor1 == valor2:
            return {
                "html": "color:yellow",
                "diferenca": "▬"
            }

def info_equipes():
    option = st.selectbox(
        "Selecione um Piloto",
        lista_id_equipe()["nomes"],
        width=250
    ) 
    persiste_option = option
    for indice, valor in enumerate(lista_id_equipe()["nomes"]):
        if valor == option:
            option = lista_id_equipe()["ids"][indice]
            break

    infos_estatisticas = estatisticas_equipe(option)
    pilotos = info_pilotos(infos_estatisticas)

    col1, col2= st.columns([2,3])
    with col1:
        container = st.container(border=True, height=300)
        with container:
            st.html(
                f"""
                <div style='padding: 0.25rem 0.5rem; height: 268px; box-sizing: border-box;
                            display: flex; flex-direction: column; justify-content: space-between;'>

                    <div style='display: flex; justify-content: space-between; align-items: flex-start;'>
                        <div>
                            <p style='margin: 0; font-size: 42px; font-weight: bold; line-height: 1.2; margin-top: 40px'>{infos_estatisticas.nome}</p>
                        </div>
                    </div>

                    <hr style='margin: 0; opacity: 0.2;'>

                    <div style='display: flex; justify-content: space-between; padding-bottom: 1.0rem;'>
                        <div>
                            <p style='margin: 0; font-size: 11px; color: gray; text-transform: uppercase; letter-spacing: 0.05em;'>Sede</p>
                            <p style='margin: 6px 0 0; font-size: 18px; font-weight: bold;'>{leitura_equipe()[option]["sede"]}</p>
                        </div>
                        <div style='text-align: center;'>
                            <p style='margin: 0; font-size: 11px; color: gray; text-transform: uppercase; letter-spacing: 0.05em;'>Proprietário</p>
                            <p style='margin: 6px 0 0; font-size: 18px; font-weight: bold;'>{leitura_equipe()[option]["proprietario"]}</p>
                        </div>
                        <div style='text-align: right;'>
                            <p style='margin: 0; font-size: 11px; color: gray; text-transform: uppercase; letter-spacing: 0.05em;'>Estreia na F1</p>
                            <p style='margin: 6px 0 0; font-size: 18px; font-weight: bold;'>{leitura_equipe()[option]["estreia"]}</p>
                        </div>
                    </div>

                </div>
                """
            )

    with col2:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            container = st.container(border=True, height=142) 
            with container:
                st.markdown(
                    f"""
                    <div class='metric-card'>
                        <p style='margin:0; font-size:16px; color:gray; margin-bottom: 15px; text-align:center;'>Posição no Campeonato</p>
                        <div>
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{infos_estatisticas.posicao}º</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )
        with col2:
            container = st.container(border=True, height=142) 
            with container:
                st.markdown(
                    f"""
                    <div class='metric-card'>
                        <p style='margin:0; font-size:16px; color:gray; margin-bottom: 15px; text-align:center;'>Pontuação</p>
                        <div>
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{infos_estatisticas.pontos}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )
        with col3:
            container = st.container(border=True, height=142) 
            with container:
                st.markdown(
                    f"""
                    <div class='metric-card'>
                        <p style='margin:0; font-size:16px; color:gray; margin-bottom: 15px; text-align:center;'>Vitórias</p>
                        <div>
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{pilotos["vitorias"]}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )
        with col4:
            container = st.container(border=True, height=142) 
            with container:
                st.markdown(
                    f"""
                    <div class='metric-card'>
                        <p style='margin:0; font-size:16px; color:gray; margin-bottom: 15px; text-align:center;'>Pódios</p>
                        <div>
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{pilotos["podios"]}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )

        col5, col6, col7, col8 = st.columns(4)
        with col5:
            container = st.container(border=True, height=142) 
            with container:
                st.markdown(
                    f"""
                    <div class='metric-card'>
                        <p style='margin:0; font-size:16px; color:gray; margin-bottom: 15px; text-align:center;'>Pole Positions</p>
                        <div>
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{pilotos["pole_positions"]}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )
        with col6:
            container = st.container(border=True, height=142) 
            with container:
                st.markdown(
                    f"""
                    <div class='metric-card'>
                        <p style='margin:0; font-size:16px; color:gray; margin-bottom: 15px; text-align:center;'>Melhor Resultado</p>
                        <div>
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{pilotos["melhor_resultado"]}º</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )
        with col7:
            container = st.container(border=True, height=142) 
            with container:
                st.markdown(
                    f"""
                    <div class='metric-card'>
                        <p style='margin:0; font-size:16px; color:gray; margin-bottom: 15px; text-align:center;'>Média de Largada</p>
                        <div>
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{pilotos["media_largada"]}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )
        with col8:
            container = st.container(border=True, height=142) 
            with container:
                st.markdown(
                    f"""
                    <div class='metric-card'>
                        <p style='margin:0; font-size:16px; color:gray; margin-bottom: 15px; text-align:center;'>Abandonos</p>
                        <div>
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{pilotos["abandonos"]}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )


    col1, col2= st.columns([2,1]) 
    with col1:
        container = st.container(border=True, height=320) 
        with container:
            rodadas = [f"GP {i["rodada"]}" for i in infos_estatisticas.info_individual_rodada["corrida"]]
            pontos = [int(i["pontos"]) for i in infos_estatisticas.info_individual_rodada["corrida"]]
            posicoes = []
            for i in infos_estatisticas.info_individual_rodada["corrida"]:
                try:
                   posicoes.append(int(i["posicao"]))
                except:
                    posicoes.append(None) 

            rotulo_gp = []
            for i in infos_estatisticas.info_individual_rodada["corrida"]:
                if corrida()[i["id_circuito"]]:
                    rotulo_gp.append(corrida()[i["id_circuito"]])
                else:
                    rotulo_gp.append(i["id_circuito"])

            dados = {
                "rodadas": rodadas,
                "posicoes": posicoes,
                "pontos": pontos
            }

            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=dados["rodadas"],
                y=dados["pontos"],
                name="Pontos",
                marker_color="#990012",
                opacity=0.8,
                customdata=rotulo_gp,
                hovertemplate="%{customdata} <br>Pontos: %{y}<extra></extra>",
            ))


            fig.add_trace(go.Scatter(
                x=dados["rodadas"],
                y=dados["posicoes"],
                mode="lines+markers",
                name="Posição",
                yaxis="y2",
                line=dict(color="#4A90D9", width=4),
                marker=dict(color="#4A90D9", size=6),
                line_shape="spline",
            ))

            fig.update_layout(
                height=280,
                title="Evolução da Equipe na Temporada",
                hovermode="x unified",
                plot_bgcolor="rgba(0,0,0,0)",
                paper_bgcolor="rgba(0,0,0,0)",
                margin=dict(l=40, r=40, t=60, b=40),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                bargap=0.3,      
                xaxis=dict(
                    tickmode="array",
                    tickvals=dados["rodadas"],
                    showgrid=False,
                ),
                yaxis=dict(
                    title="Pontos",
                    showgrid=True,
                    gridcolor="rgba(255,255,255,0.05)",
                ),
                yaxis2=dict(
                    title="Posição",
                    overlaying="y",
                    side="right",
                    autorange="reversed",
                    showgrid=False,
                ),
            )

            st.plotly_chart(fig, use_container_width=True)


    with col2:
        container = st.container(border=True, height=320) 
        with container:
            col1, col2= st.columns(2)
            with col1:
                st.markdown(
                    f"""
                    <div class='metric-card'>
                        <div>
                            <p style='font-size:16px; font-weight:bold;'>Comparação entre Equipes</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )
            with col2:
                nome_comparacao = []
                for i in lista_id_equipe()["nomes"]:
                    if i == persiste_option:
                        continue
                    else:
                        nome_comparacao.append(i)

                option = st.selectbox(
                    "",
                    nome_comparacao,
                    label_visibility="collapsed",
                    width=250
                )   

            persiste_equipe = option
            for indice, valor in enumerate(lista_id_equipe()["nomes"]):
                if valor == option:
                    option = lista_id_equipe()["ids"][indice]
                    break

            infos_estatisticas_equipe = estatisticas_equipe(option)
            equipe_compara = info_pilotos(infos_estatisticas_equipe)

            linhas_html = f"""
            <tr>
                <td style='font-weight:bold;'></td>
                <td style='font-weight:bold;'>{persiste_option}</td>
                <td style='font-weight:bold;'>{persiste_equipe}</td>
                <td style='font-weight:bold;'>Diferença</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Posição Campeonato</td>
                <td style='font-weight:bold; text-align:left'>{infos_estatisticas.posicao}º</td>
                <td style='font-weight:bold;'>{infos_estatisticas_equipe.posicao}º</td>
                <td style='font-weight:bold; {calculo_diferenca(infos_estatisticas.posicao, infos_estatisticas_equipe.posicao, False)["html"]};'>{calculo_diferenca(infos_estatisticas.posicao, infos_estatisticas_equipe.posicao, False)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Pontuação</td>
                <td style='font-weight:bold;'>{infos_estatisticas.pontos}</td>
                <td style='font-weight:bold;'>{infos_estatisticas_equipe.pontos}</td>
                <td style='font-weight:bold; {calculo_diferenca(infos_estatisticas.pontos, infos_estatisticas_equipe.pontos, True)["html"]};'>{calculo_diferenca(infos_estatisticas.pontos, infos_estatisticas_equipe.pontos, True)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Vitórias</td>
                <td style='font-weight:bold;'>{pilotos["vitorias"]}</td>
                <td style='font-weight:bold;'>{equipe_compara["vitorias"]}</td>
                <td style='font-weight:bold; {calculo_diferenca(pilotos["vitorias"], equipe_compara["vitorias"], True)["html"]};'>{calculo_diferenca(pilotos["vitorias"], equipe_compara["vitorias"], True)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Pódios</td>
                <td style='font-weight:bold;'>{pilotos["podios"]}</td>
                <td style='font-weight:bold;'>{equipe_compara["podios"]}</td>
                <td style='font-weight:bold; {calculo_diferenca(pilotos["podios"], equipe_compara["podios"], True)["html"]};'>{calculo_diferenca(pilotos["podios"], equipe_compara["podios"], True)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Pole Positions</td>
                <td style='font-weight:bold;'>{pilotos["pole_positions"]}</td>
                <td style='font-weight:bold;'>{equipe_compara["pole_positions"]}</td>
                <td style='font-weight:bold; {calculo_diferenca(pilotos["pole_positions"], equipe_compara["pole_positions"], True)["html"]};'>{calculo_diferenca(pilotos["pole_positions"], equipe_compara["pole_positions"], True)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Média de Largada</td>
                <td style='font-weight:bold;'>{pilotos["media_largada"]}</td>
                <td style='font-weight:bold;'>{equipe_compara["media_largada"]}</td>
                <td style='font-weight:bold; {calculo_diferenca(pilotos["media_largada"], equipe_compara["media_largada"], False)["html"]};'>{calculo_diferenca(pilotos["media_largada"], equipe_compara["media_largada"], False)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Abandonos</td>
                <td style='font-weight:bold;'>{pilotos["abandonos"]}</td>
                <td style='font-weight:bold;'>{equipe_compara["abandonos"]}</td>
                <td style='font-weight:bold; {calculo_diferenca(pilotos["abandonos"], equipe_compara["abandonos"], False)["html"]};'>{calculo_diferenca(pilotos["abandonos"], equipe_compara["abandonos"], False)["diferenca"]}</td>
            </tr>
            """

            tabela_html = f"""
                <style>
                    .f1-table {{
                        width: 100%;
                        border-collapse: collapse;
                        font-family: sans-serif;
                        font-size: 12px;
                    }}
                    .f1-table td {{
                        padding: 3px 15px;
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
            st.html(tabela_html)
    
    container = st.container(border=True, height=325) 
    with container:
        from services.calendario_service import rodadas

        infos_rodada = rodadas()
        total_rodadas = infos_rodada.round

        num_titular = int(total_rodadas)*0.4

        info_duelo = []
        for i in infos_estatisticas.piloto_id:
            duelo = estatisticas_piloto(i)
            qtde_duelo = duelo.pontuacao_individual
            if len(qtde_duelo) > num_titular:
                info_duelo.append({
                    "nome": f"{duelo.nome} {duelo.sobrenome}",
                    "pontos": duelo.pontos,
                    "numero": duelo.numero,
                    "podios": duelo.podios,
                    "melhor_resultado": duelo.melhor_resultado,
                    "media_grid": duelo.media_largada,
                    "abandonos": duelo.abandonos,
                    "pole_position": duelo.pole_positions,
                    "pontos_medios": float(duelo.pontos) / total_rodadas
                })

        st.markdown(
        f"""
            <div class='metric-card'>
                <p style='margin:0; font-size:16px; margin-bottom: 15px; text-align:left; color:gray'>Duelo interno - {ano_atual}</p>
            </div>
        """, unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns(3) 
        with col1:
            st.markdown(
            f"""
                <div class='metric-card'>
                    <p style='margin:0; font-size:16px; margin-bottom: 5px; text-align:left; font-weight:bold; color:#990012;'>Nº {info_duelo[0]["numero"]}</p>
                    <p style='margin:0; font-size:20px; margin-bottom: 5px; text-align:left; font-weight:bold; color:#990012;'>N {info_duelo[0]["nome"]}</p>
                    <p style='margin:0; font-size:25px; margin-bottom: 5px; text-align:left; font-weight:bold; color:#990012;'>{info_duelo[0]["pontos"]} pts</p>
                    <p style='margin:0; font-size:16px; margin-bottom: 5px; text-align:left; color:gray'>{((int(info_duelo[0]["pontos"])/int(infos_estatisticas.pontos)) * 100):.1f}% da equipe</p>
                </div>
            """, unsafe_allow_html=True
            )
        with col2:
            st.html(f"""
                <div style='display:flex; justify-content:center; align-items:center; height:100%;'>
                    <span style='font-size: 30px; padding: 4px 12px; border-radius: 999px; border: 1px solid #e0e0e0; color: #888; font-weight: bold; text-align: center'>
                        vs
                    </span>
                </div>
            """)
        with col3:
            st.markdown(
            f"""
                <div class='metric-card'>
                    <p style='margin:0; font-size:16px; margin-bottom: 5px; text-align:right; font-weight:bold;'>Nº {info_duelo[1]["numero"]}</p>
                    <p style='margin:0; font-size:20px; margin-bottom: 5px; text-align:right; font-weight:bold;'>{info_duelo[1]["nome"]}</p>
                    <p style='margin:0; font-size:25px; margin-bottom: 5px; text-align:right; font-weight:bold;'>{info_duelo[1]["pontos"]} pts</p>
                    <p style='margin:0; font-size:16px; margin-bottom: 5px; text-align:right; color:gray'>{((int(info_duelo[1]["pontos"])/int(infos_estatisticas.pontos)) * 100):.1f}% da equipe</p>
                </div>
            """, unsafe_allow_html=True
            )

        st.html("<hr style='margin: 0; opacity: 0.2;'>")

        st.html(
            f"""
            <div style='padding: 2px 0 15px; gap: 10px'>
                <div style='display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 10px; margin-top: 10px'>
                    <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                        <p style='margin: 0; font-size: 16px; color: #888; text-align: center'>PÓDIOS</p>
                            <div style='display: flex; align-items: center; justify-content: space-between'>
                                <span style='font-size: 18px; font-weight: 700; color:#990012;'>{info_duelo[0]["podios"]}</span>
                                <span style='color: #444; font-size: 14px'>×</span>
                                <span style='font-size: 18px; font-weight: 700;'>{info_duelo[1]["podios"]}</span>
                            </div>
                    </div>
                    <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                        <p style='margin: 0; font-size: 16px; color: #888; text-align: center'>MELHOR RESULTADO</p>
                            <div style='display: flex; align-items: center; justify-content: space-between'>
                                <span style='font-size: 18px; font-weight: 700; color:#990012;'>{info_duelo[0]["melhor_resultado"]}</span>
                                <span style='color: #444; font-size: 14px'>×</span>
                                <span style='font-size: 18px; font-weight: 700;'>{info_duelo[1]["melhor_resultado"]}</span>
                            </div>
                    </div>
                    <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                        <p style='margin: 0; font-size: 16px; color: #888; text-align: center'>MÉDIA DE LARGADA</p>
                            <div style='display: flex; align-items: center; justify-content: space-between'>
                                <span style='font-size: 18px; font-weight: 700; color:#990012;'>{info_duelo[0]["media_grid"]}</span>
                                <span style='color: #444; font-size: 14px'>×</span>
                                <span style='font-size: 18px; font-weight: 700;'>{info_duelo[1]["media_grid"]}</span>
                            </div>
                    </div>
                    <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                        <p style='margin: 0; font-size: 16px; color: #888; text-align: center'>PTS MÉDIOS/GP</p>
                            <div style='display: flex; align-items: center; justify-content: space-between'>
                                <span style='font-size: 18px; font-weight: 700; color:#990012;'>{int(info_duelo[0]["pontos"]) / total_rodadas}</span>
                                <span style='color: #444; font-size: 14px'>×</span>
                                <span style='font-size: 18px; font-weight: 700;'>{int(info_duelo[1]["pontos"]) / total_rodadas}</span>
                            </div>
                    </div>
                </div>
            </div>
            """
        )