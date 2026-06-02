import streamlit as st

from services.equipes_service import lista_id_equipe, estatisticas_equipe
from services.piloto_services import estatisticas_piloto
from utils.acesso_equipes import leitura_equipe

def info_equipes():
    option = st.selectbox(
        "Selecione um Piloto",
        lista_id_equipe()["nomes"],
        width=250
    ) 

    for indice, valor in enumerate(lista_id_equipe()["nomes"]):
        if valor == option:
            option = lista_id_equipe()["ids"][indice]
            break

    infos_estatisticas = estatisticas_equipe(option)
    
    # Pegando id valido
    pilotos = []
    for i in infos_estatisticas.piloto_id:
        try:
            estatisticas_piloto(i)
            pilotos.append(i)
        except:
            continue


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
                            <p style='margin: 0; font-size: 34px; font-weight: bold; line-height: 1.2;'>{infos_estatisticas.nome}</p>
                        </div>
                    </div>

                    <hr style='margin: 0; opacity: 0.2;'>

                    <div style='display: flex; justify-content: space-between; padding-bottom: 1.0rem;'>
                        <div>
                            <p style='margin: 0; font-size: 11px; color: gray; text-transform: uppercase; letter-spacing: 0.05em;'>Sede</p>
                            <p style='margin: 6px 0 0; font-size: 24px; font-weight: bold;'>{leitura_equipe()[option]["sede"]}</p>
                        </div>
                        <div style='text-align: center;'>
                            <p style='margin: 0; font-size: 11px; color: gray; text-transform: uppercase; letter-spacing: 0.05em;'>Proprietário</p>
                            <p style='margin: 6px 0 0; font-size: 24px; font-weight: bold;'>{leitura_equipe()[option]["proprietario"]}</p>
                        </div>
                        <div style='text-align: right;'>
                            <p style='margin: 0; font-size: 11px; color: gray; text-transform: uppercase; letter-spacing: 0.05em;'>Estreia na F1</p>
                            <p style='margin: 6px 0 0; font-size: 24px; font-weight: bold;'>{leitura_equipe()[option]["estreia"]}</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>infos_estatisticas.pontos</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>infos_estatisticas.vitorias</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>infos_estatisticas.podios</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>infos_estatisticas.pole_positions</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>infos_estatisticas.melhor_resultadoº</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>infos_estatisticas.media_largada</p>
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
                            <p style='margin:0; font-size:36px; font-weight:bold; text-align:center;'>infos_estatisticas.abandonos</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )