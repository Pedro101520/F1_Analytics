import streamlit as st
import plotly.graph_objects as go
from utils.acesso_corrida import corrida

from services.piloto_services import estatisticas_piloto, lista_id

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


def info_pilotos():
    option = st.selectbox(
        "Selecione um Piloto",
        lista_id()["nomes"],
        width=250
    )   

    persiste_option = option
    for indice, valor in enumerate(lista_id()["nomes"]):
        if valor == option:
            option = lista_id()["ids"][indice]
            break

    infos_estatisticas = estatisticas_piloto(option)

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
                            <p style='margin: 0; font-size: 20px; line-height: 1.2;'>{infos_estatisticas.nome}</p>
                            <p style='margin: 0; font-size: 34px; font-weight: bold; line-height: 1.2;'>{infos_estatisticas.sobrenome}</p>
                        </div>
                        <span style='font-size: 18px; font-weight: bold; padding: 4px 12px;
                                    border-radius: 999px; background: #FFE5E8; color: #990012; letter-spacing: 0.05em;'>
                            Nº {infos_estatisticas.numero}
                        </span>
                    </div>

                    <div style='display: flex; gap: 8px;'>
                        <span style='font-size: 12px; padding: 4px 12px; border-radius: 999px; border: 1px solid #e0e0e0; color: #990012; background: #FFE5E8; font-weight: bold;'>
                            {infos_estatisticas.nacionalidade}
                        </span>
                        <span style='font-size: 12px; padding: 4px 12px; border-radius: 999px; border: 1px solid #e0e0e0; color: #990012; background: #FFE5E8; font-weight: bold;'>
                            {infos_estatisticas.equipe}
                        </span>
                        <span style='font-size: 12px; padding: 4px 12px; border-radius: 999px; border: 1px solid #e0e0e0; color: #990012; background: #FFE5E8; font-weight: bold;'>
                            {infos_estatisticas.sigla}
                        </span>
                    </div>

                    <hr style='margin: 0; opacity: 0.2;'>

                    <div style='display: flex; justify-content: space-between; padding-bottom: 1.0rem;'>
                        <div>
                            <p style='margin: 0; font-size: 11px; color: gray; text-transform: uppercase; letter-spacing: 0.05em;'>Idade</p>
                            <p style='margin: 6px 0 0; font-size: 24px; font-weight: bold;'>{infos_estatisticas.idade}</p>
                        </div>
                        <div style='text-align: center;'>
                            <p style='margin: 0; font-size: 11px; color: gray; text-transform: uppercase; letter-spacing: 0.05em;'>Estreia na F1</p>
                            <p style='margin: 6px 0 0; font-size: 24px; font-weight: bold;'>{infos_estatisticas.estreia}</p>
                        </div>
                        <div style='text-align: right;'>
                            <p style='margin: 0; font-size: 11px; color: gray; text-transform: uppercase; letter-spacing: 0.05em;'>Títulos Mundiais</p>
                            <p style='margin: 6px 0 0; font-size: 24px; font-weight: bold;'>{infos_estatisticas.qtde_mundial}</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{infos_estatisticas.vitorias}</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{infos_estatisticas.podios}</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{infos_estatisticas.pole_positions}</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{infos_estatisticas.melhor_resultado}º</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{infos_estatisticas.media_largada}</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>{infos_estatisticas.abandonos}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )

    col1, col2= st.columns([2,1]) 
    with col1:
        container = st.container(border=True, height=320) 
        with container:
            rodadas = [f"GP {i["round"]}" for i in infos_estatisticas.pontuacao_individual]
            pontos = [int(i["ponto_por_corrida"]) + int(i["pontos_por_sprint"]) for i in infos_estatisticas.pontuacao_individual]
            posicoes = []
            for i in infos_estatisticas.pontuacao_individual:
                try:
                   posicoes.append(int(i["posicao"]))
                except:
                    posicoes.append(None) 

            rotulo_gp = []
            for i in infos_estatisticas.pontuacao_individual:
                if corrida()[i["id_gp"]]:
                    rotulo_gp.append(corrida()[i["id_gp"]])
                else:
                    rotulo_gp.append(i["id_gp"])

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
                title="Evolução do Piloto na Temporada",
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
                            <p style='font-size:16px; font-weight:bold;'>Comparação entre pilotos</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )
            with col2:
                nome_comparacao = []
                for i in lista_id()["nomes"]:
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

            persiste_piloto = option
            for indice, valor in enumerate(lista_id()["nomes"]):
                if valor == option:
                    option = lista_id()["ids"][indice]
                    break

            infos_estatisticas_piloto = estatisticas_piloto(option)

            linhas_html = f"""
            <tr>
                <td style='font-weight:bold;'></td>
                <td style='font-weight:bold;'>{persiste_option}</td>
                <td style='font-weight:bold;'>{persiste_piloto}</td>
                <td style='font-weight:bold;'>Diferença</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Posição Campeonato</td>
                <td style='font-weight:bold; text-align:left'>{infos_estatisticas.posicao}</td>
                <td style='font-weight:bold;'>{infos_estatisticas_piloto.posicao}</td>
                <td style='font-weight:bold; {calculo_diferenca(infos_estatisticas.posicao, infos_estatisticas_piloto.posicao, False)["html"]};'>{calculo_diferenca(infos_estatisticas.posicao, infos_estatisticas_piloto.posicao, False)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Pontuação</td>
                <td style='font-weight:bold;'>{infos_estatisticas.pontos}</td>
                <td style='font-weight:bold;'>{infos_estatisticas_piloto.pontos}</td>
                <td style='font-weight:bold; {calculo_diferenca(infos_estatisticas.pontos, infos_estatisticas_piloto.pontos, True)["html"]};'>{calculo_diferenca(infos_estatisticas.pontos, infos_estatisticas_piloto.pontos, True)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Vitórias</td>
                <td style='font-weight:bold;'>{infos_estatisticas.vitorias}</td>
                <td style='font-weight:bold;'>{infos_estatisticas_piloto.vitorias}</td>
                <td style='font-weight:bold; {calculo_diferenca(infos_estatisticas.vitorias, infos_estatisticas_piloto.vitorias, True)["html"]};'>{calculo_diferenca(infos_estatisticas.vitorias, infos_estatisticas_piloto.vitorias, True)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Pódios</td>
                <td style='font-weight:bold;'>{infos_estatisticas.podios}</td>
                <td style='font-weight:bold;'>{infos_estatisticas_piloto.podios}</td>
                <td style='font-weight:bold; {calculo_diferenca(infos_estatisticas.podios, infos_estatisticas_piloto.podios, True)["html"]};'>{calculo_diferenca(infos_estatisticas.podios, infos_estatisticas_piloto.podios, True)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Pole Positions</td>
                <td style='font-weight:bold;'>{infos_estatisticas.pole_positions}</td>
                <td style='font-weight:bold;'>{infos_estatisticas_piloto.pole_positions}</td>
                <td style='font-weight:bold; {calculo_diferenca(infos_estatisticas.pole_positions, infos_estatisticas_piloto.pole_positions, True)["html"]};'>{calculo_diferenca(infos_estatisticas.pole_positions, infos_estatisticas_piloto.pole_positions, True)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Média de Largada</td>
                <td style='font-weight:bold;'>{infos_estatisticas.media_largada}</td>
                <td style='font-weight:bold;'>{infos_estatisticas_piloto.media_largada}</td>
                <td style='font-weight:bold; {calculo_diferenca(infos_estatisticas.media_largada, infos_estatisticas_piloto.media_largada, False)["html"]};'>{calculo_diferenca(infos_estatisticas.media_largada, infos_estatisticas_piloto.media_largada, False)["diferenca"]}</td>
            </tr>
            <tr>
                <td style='font-weight:bold;'>Abandonos</td>
                <td style='font-weight:bold;'>{infos_estatisticas.abandonos}</td>
                <td style='font-weight:bold;'>{infos_estatisticas_piloto.abandonos}</td>
                <td style='font-weight:bold; {calculo_diferenca(infos_estatisticas.abandonos, infos_estatisticas_piloto.abandonos, False)["html"]};'>{calculo_diferenca(infos_estatisticas.abandonos, infos_estatisticas_piloto.abandonos, False)["diferenca"]}</td>
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
        st.markdown(
            f"""
            <div class='metric-card'>
                <div>
                    <p style='margin:0; font-size:20px; font-weight:bold;'>Líder do Campeonato:</p>
                    <p style='margin:4px 0 0 0; font-size:26px; font-weight:bold;'></p>
                </div>
                <p style='margin:0; font-size:16px; color:gray; margin-bottom: 25px;'>pontos</p>
            </div>
            """, unsafe_allow_html=True
        )