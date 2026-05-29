import streamlit as st

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
                        <span style='font-size: 12px; padding: 4px 12px; border-radius: 999px; border: 1px solid #e0e0e0; color: gray;'>
                            {infos_estatisticas.nacionalidade}
                        </span>
                        <span style='font-size: 12px; padding: 4px 12px; border-radius: 999px; border: 1px solid #e0e0e0; color: gray;'>
                            {infos_estatisticas.equipe}
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
                            <p style='margin: 6px 0 0; font-size: 24px; font-weight: bold;'>infos_estatisticas.mundial</p>
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
                        <div>
                            <p style='margin:0; font-size:20px; font-weight:bold;'>Líder do Campeonato:</p>
                            <p style='margin:4px 0 0 0; font-size:26px; font-weight:bold;'></p>
                        </div>
                        <p style='margin:0; font-size:16px; color:gray; margin-bottom: 25px;'>pontos</p>
                    </div>
                    """, unsafe_allow_html=True
                )
        with col2:
            container = st.container(border=True, height=142) 
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
        with col3:
            container = st.container(border=True, height=142) 
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
        with col4:
            container = st.container(border=True, height=142) 
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

        col5, col6, col7, col8 = st.columns(4)
        with col5:
            container = st.container(border=True, height=142) 
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
        with col6:
            container = st.container(border=True, height=142) 
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
        with col7:
            container = st.container(border=True, height=142) 
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
        with col8:
            container = st.container(border=True, height=142) 
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


    col1, col2= st.columns([2,1]) 
    with col1:
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