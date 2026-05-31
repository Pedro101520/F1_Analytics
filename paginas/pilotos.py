import streamlit as st
import plotly.graph_objects as go

from services.piloto_services import estatisticas_piloto, lista_id

def info_pilotos():
    st.write("")
    option = st.selectbox(
        "Selecione um Piloto",
        lista_id(),
        width=250
    )   

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
        container = st.container(border=True, height=300) 
        with container:
            rodadas = [i["round"] for i in infos_estatisticas.pontuacao_individual]
            pontos = [i["ponto_por_corrida"] for i in infos_estatisticas.pontuacao_individual]
            posicoes = []
            for i in infos_estatisticas.pontuacao_individual:
                try:
                   posicoes.append(int(i["posicao"]))
                except:
                    posicoes.append(None) 

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
        container = st.container(border=True, height=300) 
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