import streamlit as st
from services.calendario_service import rodadas
from services.piloto_services import piloto_lider
from services.resultados_service import resultados_corrida

infos_rodada = rodadas()
infos_lider = piloto_lider()
infos_results = resultados_corrida()

total_rodadas = infos_rodada.total_rodadas
rodada_atual = infos_rodada.round
prox_circuito = infos_rodada.circuito
prox_corrida = infos_rodada.prox_corrida

lider_atual = infos_lider.lider
pontuacao_lider = infos_lider.pontos

ultimo_circuito = infos_results.ultima_pista
ultimo_ganhador = infos_results.vitoria

def pagina_inicial():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        # height=500, esse código define o tamanho vertical do container
        container = st.container(border=True)
        container.markdown(
            f"""
                <h4 style='margin: -20px; padding:20px; font-size: 16px'>Rodada Atual:</h4>
                <div style='display: flex; gap: 0px;'>
                    <h4 style='margin:0; padding:0; color: #990012;'>GP</h4>
                    <h4 style='margin:0; padding:0; color: #990012; font-weight: bold;'>{rodada_atual} / {total_rodadas}</h4>
                </div>
            """,
            unsafe_allow_html=True
        )
        container.write("")
        container.caption(f"de {total_rodadas} corridas")
    with col2:
        container = st.container(border=True)
        container.markdown(
            f"""
                <h4 style='margin: -20px; padding:20px; font-size: 16px'>Líder do Campeonato:</h4>
                <div style='display: flex; gap: 0px;'>
                    <h4 style='margin:0; padding:0;'>{lider_atual}</h4>
                </div>
            """,
            unsafe_allow_html=True
        )
        container.write("")
        container.caption(f"{pontuacao_lider} pontos")
    with col3:
        container = st.container(border=True)
        container.markdown(
            f"""
                <h4 style='margin: -20px; padding:20px; font-size: 16px'>Próxima Corrida:</h4>
                <div style='display: flex; gap: 0px;'>
                    <h4 style='margin:0; padding:0; color: #990012; font-weight: bold;'>{prox_circuito}</h4>
                </div>
            """,
            unsafe_allow_html=True
        )
        container.write("")
        container.caption(f"Em {prox_corrida} dias")
    with col4:
        container = st.container(border=True)
        container.markdown(
            f"""
                <h4 style='margin: -20px; padding:20px; font-size: 16px'>Última Vitória:</h4>
                <div style='display: flex; gap: 0px;'>
                    <h4 style='margin:0; padding:0; font-weight: bold;'>{ultimo_ganhador}</h4>
                </div>
            """,
            unsafe_allow_html=True
        )
        container.write("")
        container.caption(f"{ultimo_circuito}")

    # st.table(
    #     {
    #         ":material/folder: Project": "**Streamlit** - The fastest way to build data apps",
    #         ":material/code: Repository": "[github.com/streamlit/streamlit](https://github.com/streamlit/streamlit)",
    #         ":material/new_releases: Version": ":gray-badge[1.45.0]",
    #         ":material/license: License": ":green-badge[Apache 2.0]",
    #         ":material/group: Maintainers": ":blue-badge[Core Team] :violet-badge[Community]",
    #     },
    #     border="horizontal"
    # )