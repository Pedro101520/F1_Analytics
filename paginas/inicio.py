import streamlit as st
from services.calendario_service import rodadas
from services.piloto_services import piloto_lider
from services.resultados_service import resultados_corrida
from services.clima_service import clima

infos_rodada = rodadas()
infos_lider = piloto_lider()
infos_results = resultados_corrida()
info_clima = clima()

total_rodadas = infos_rodada.total_rodadas
rodada_atual = infos_rodada.round
prox_circuito = infos_rodada.circuito
prox_corrida = infos_rodada.prox_corrida
proxima_cidade = infos_rodada.localidade
prox_data = infos_rodada.prox_corrida_data

lider_atual = infos_lider.lider
pontuacao_lider = infos_lider.pontos

ultimo_circuito = infos_results.ultima_pista
ultimo_ganhador = infos_results.vitoria

temperatura = info_clima.temperatura
umidade = info_clima.umidade
vento = info_clima.vento
chuva = info_clima.chuva
clima_code = info_clima.clima_texto
raio_uv = info_clima.uv

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

    with col1:
        st.container(border=True).markdown(
            f"""
            <div class='metric-card'>
                <div>
                    <p style='margin:0; font-size:16px; font-weight:bold;'>Rodada Atual:</p>
                    <p style='margin:4px 0 0 0; color:#990012; font-size:20px; font-weight:bold;'>GP {rodada_atual}</p>
                </div>
                <p style='margin:0; font-size:12px; color:gray; margin-bottom: 25px;'>de {total_rodadas} corridas</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        st.container(border=True).markdown(
            f"""
            <div class='metric-card'>
                <div>
                    <p style='margin:0; font-size:13px; font-weight:bold;'>Líder do Campeonato:</p>
                    <p style='margin:4px 0 0 0; font-size:20px; font-weight:bold;'>{lider_atual}</p>
                </div>
                <p style='margin:0; font-size:12px; color:gray; margin-bottom: 25px;'>{pontuacao_lider} pontos</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col3:
        st.container(border=True).markdown(
            f"""
            <div class='metric-card'>
                <div>
                    <p style='margin:0; font-size:13px; font-weight:bold;'>Próxima Corrida:</p>
                    <p style='margin:4px 0 0 0; color:#990012; font-size:20px; font-weight:bold;'>{prox_circuito}</p>
                </div>
                <p style='margin:0; font-size:12px; color:gray; margin-bottom: 25px;'>Em {prox_corrida} dias</p>
            </div>
            """, unsafe_allow_html=True
        )

    with col4:
        st.container(border=True).markdown(
            f"""
            <div class='metric-card'>
                <div>
                    <p style='margin:0; font-size:13px; font-weight:bold;'>Última Vitória:</p>
                    <p style='margin:4px 0 0 0; font-size:20px; font-weight:bold;'>{ultimo_ganhador}</p>
                </div>
                <p style='margin:0; font-size:12px; color:gray; margin-bottom: 25px;'>{ultimo_circuito}</p>
            </div>
            """, unsafe_allow_html=True
        )

    col5, col6= st.columns(2)
    with col5:
        with st.container(border=True):
            st.html(
                f"""
                <div style='padding: 4px 0 12px;'>

                    <div style='display: flex; align-items: center; gap: 8px; margin-bottom: 16px;'>
                        <span style='font-size: 16px; color: #aaa;'>Previsão do Tempo —</span>
                        <span style='font-size: 16px; font-weight: 600;'>{prox_circuito} · {proxima_cidade}</span>
                    </div>

                    <div style='display: flex; align-items: center; gap: 14px; margin-bottom: 16px;'>
                        <h2 style='font-size: 48px; margin: 0; padding: 0; font-weight: 700;'>{round(temperatura)}°C</h2>
                        <div>
                            <p style='margin: 0; font-size: 18px; font-weight: 600;'>{clima_code}</p>
                            <p style='margin: 4px 0 0; font-size: 13px; color: #aaa;'>{prox_data} · dia da corrida</p>
                        </div>
                    </div>

                    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 10px;'>
                        <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                            <p style='margin: 0; font-size: 12px; color: #888;'>Chuva</p>
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
    # container.write("")
    with col6:
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
        # container.write("")
        container.caption(f"{pontuacao_lider} pontos")

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