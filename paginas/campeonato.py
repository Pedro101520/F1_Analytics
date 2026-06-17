import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

from services.campeonato_service import info_campeonato
from services.metricas_service import info_metricas
from services.predicao_service import info_pred
from services.piloto_services import estatisticas_piloto

info_camp = info_campeonato()
metricas = info_metricas()
predicao = info_pred()

ano_atual = datetime.now().year

def info_exibe():
    if st.session_state.dados == "pilotos":
        tabela_pilotos = [i["nome"] for i in info_camp.tabela_pilotos]
        top10 = tabela_pilotos[:10]
        top10_invertido = top10[::-1]

        pontos = [int(i["pontos"]) for i in info_camp.tabela_pilotos]
        pontos = pontos[:10]
        pontos = pontos[::-1]

        return top10_invertido, pontos
    else:
        tabela_equipes = [i["nome"] for i in info_camp.tabela_equipes]
        top10 = tabela_equipes[:10]
        top10_invertido = top10[::-1]

        pontos = [int(i["pontos"]) for i in info_camp.tabela_equipes]
        pontos = pontos[:10]
        pontos = pontos[::-1]

        return top10_invertido, pontos

def info_exibe_tabela():
        if st.session_state.dados == "pilotos":
            tabela_pilotos = [i["nome"] for i in info_camp.tabela_pilotos]
            top3 = tabela_pilotos[:3]

            pontos = [int(i["pontos"]) for i in info_camp.tabela_pilotos]
            pontos = pontos[:3]

            return top3, pontos
        else:
            tabela_equipes = [i["nome"] for i in info_camp.tabela_equipes]
            top3 = tabela_equipes[:3]

            pontos = [int(i["pontos"]) for i in info_camp.tabela_equipes]
            pontos = pontos[:3]   

            return top3, pontos    

def info_html():
    if st.session_state.dados == "pilotos":
        linhas_html = f"""
            <tr>
                <td style='font-weight:bold;'>#</td>
                <td style='font-weight:bold;'>Piloto</td>
                <td style='font-weight:bold;'>Equipe</td>
                <td style='font-weight:bold;'>Nacionalidade</td>
                <td style='font-weight:bold;'>Pontos</td>
                <td style='font-weight:bold;'>Vitórias</td>
            </tr>
        """

        linhas_html += f"""
            <tr>
                <td style='color:#990012; font-weight:bold;'>1</td>
                <td style='color:#990012; font-weight:bold;'>{info_camp.tabela_pilotos[0]["nome"]}</td>
                <td style='color:#990012; font-weight:bold;'>{info_camp.tabela_pilotos[0]["equipe"]}</td>
                <td style='color:#990012; font-weight:bold;'>{info_camp.tabela_pilotos[0]["pais"]}</td>
                <td style='color:#990012; font-weight:bold;'>{info_camp.tabela_pilotos[0]["pontos"]}</td>
                <td style='color:#990012; font-weight:bold;'>{info_camp.tabela_pilotos[0]["vitorias"]}</td>
            </tr>  
        """  

        for indice, i in enumerate(info_camp.tabela_pilotos[1:]):
            linhas_html += f"""
                <tr>
                    <td>{indice + 2}</td>
                    <td>{i["nome"]}</td>
                    <td>{i["equipe"]}</td>
                    <td>{i["pais"]}</td>
                    <td>{i["pontos"]}</td>
                    <td>{i["vitorias"]}</td>
                </tr>
            """   
        return linhas_html
    else:
        linhas_html = f"""
            <tr>
                <td style='font-weight:bold;'>#</td>
                <td style='font-weight:bold;'>Piloto</td>
                <td style='font-weight:bold;'>Nacionalidade</td>
                <td style='font-weight:bold;'>Pontos</td>
                <td style='font-weight:bold;'>Vitórias</td>
            </tr>
        """

        linhas_html += f"""
            <tr>
                <td style='color:#990012; font-weight:bold;'>1</td>
                <td style='color:#990012; font-weight:bold;'>{info_camp.tabela_equipes[0]["nome"]}</td>
                <td style='color:#990012; font-weight:bold;'>{info_camp.tabela_equipes[0]["pais"]}</td>
                <td style='color:#990012; font-weight:bold;'>{info_camp.tabela_equipes[0]["pontos"]}</td>
                <td style='color:#990012; font-weight:bold;'>{info_camp.tabela_equipes[0]["vitorias"]}</td>
            </tr>  
        """  

        for indice, i in enumerate(info_camp.tabela_equipes[1:]):
            linhas_html += f"""
                <tr>
                    <td>{indice + 2}</td>
                    <td>{i["nome"]}</td>
                    <td>{i["pais"]}</td>
                    <td>{i["pontos"]}</td>
                    <td>{i["vitorias"]}</td>
                </tr>
            """   

        return linhas_html


def camp():
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Piloto", use_container_width=True):
            st.session_state.dados = "pilotos"
            st.rerun()
    with col2:
        if st.button("Equipe", use_container_width=True):
            st.session_state.dados = "equipes"
            st.rerun()

    col3, col4 = st.columns(2)
    with col3:
        container = st.container(border=True, height=450)
        with container:

            linhas_html = info_html()

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
                    <span style='font-size: 20px; font-weight: 600;'>Classificação de Pilotos:</span>
                </div>
            """)              
            st.html(tabela_html)
    
    with col4:
        container = st.container(border=True, height=450)
        with container:
            top10_invertido, pontos = info_exibe()

            fig = go.Figure(go.Bar(
                x=pontos,
                y=top10_invertido,
                orientation="h",
                marker_color="#990012",
                text=pontos,
                textposition="inside",
                textfont=dict(color="white", size=12),
            ))

            fig.update_layout(
                title="PONTOS — TOP 10",
                title_font=dict(size=20),
                margin=dict(l=10, r=20, t=40, b=10),
                height=400,
                xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
                yaxis=dict(showgrid=False, tickfont=dict(size=12)),
            )

            st.plotly_chart(fig, use_container_width=True)
    
    container = st.container(border=True, height=200) 
    with container:
        top3, pontos = info_exibe_tabela()

        st.markdown(
            f"""
            <div class='metric-card'>
                <div>
                    <p style='margin:0; font-size:16px; margin-bottom: 15px; text-align:left;'>Pódio da Temporada</p>
                </div>
            </div>
            """, unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns(3)
        with col1:
            container = st.container(border=True, height=115) 
            with container:
                st.markdown(
                    f"""
                    <div>
                        <p style='margin:0; font-size:40px; color:#808080; margin-bottom: 0px; margin-top: -15px; text-align:center; font-weight:bold;'>2º</p>
                        <p style='margin:0; font-size:18px; margin-bottom: 18px; text-align:center; font-weight:bold;'>{top3[1]}</p>
                    </div>
                    """, unsafe_allow_html=True
                )
        with col2:
            container = st.container(border=True, height=115) 
            with container:
                st.markdown(
                    f"""
                    <div>
                        <p style='margin:0; font-size:40px; color:#B8860B; margin-bottom: 0px; margin-top: -15px; text-align:center; font-weight:bold;'>1º</p>
                        <p style='margin:0; font-size:18px; margin-bottom: 18px; text-align:center; font-weight:bold;'>{top3[0]}</p>
                    </div>
                    """, unsafe_allow_html=True
                )
        with col3:
            container = st.container(border=True, height=115) 
            with container:
                st.markdown(
                    f"""
                    <div>
                        <p style='margin:0; font-size:40px; color:#8B4513; margin-bottom: 0px; margin-top: -15px; text-align:center; font-weight:bold;'>3º</p>
                        <p style='margin:0; font-size:18px; margin-bottom: 18px; text-align:center; font-weight:bold;'>{top3[2]}</p>
                    </div>
                    """, unsafe_allow_html=True
                )

    container = st.container(border=True, height=300) 
    with container:
        col5, col6 = st.columns(2)
        with col5:
            quali = ""
            if predicao.valores_pred[0]["quali"] == "False":
                f1_score = metricas.sem_quali["f1-score"]
                recall = metricas.sem_quali["recall"]
                presicao = metricas.sem_quali["precision"]
                acuracia = metricas.sem_quali["accuracy"]
                quali = "Pré-qualifying"
            else:
                f1_score = metricas.com_quali["f1-score"]
                recall = metricas.com_quali["recall"]
                presicao = metricas.com_quali["precision"]
                acuracia = metricas.com_quali["accuracy"]
                quali = "Pós-qualifying"

            st.html(
                f"""
                <div style='padding: 4px 0 12px; gap: 30px'>
                    <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 5px'>
                        <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                            <p style='margin: 0; font-size: 16px; color: #888;'>Acurácia</p>
                            <p style='margin: 4px 0 0; font-size: 18px; font-weight: 700;'>{round(float(acuracia * 100), 2)}</p>
                        </div>
                        <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                            <p style='margin: 0; font-size: 12px; color: #888;'>F1-Score</p>
                            <p style='margin: 4px 0 0; font-size: 18px; font-weight: 700;'>{round(float(f1_score * 100), 2)}</p>
                        </div>
                        <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                            <p style='margin: 0; font-size: 12px; color: #888;'>Precisão</p>
                            <p style='margin: 4px 0 0; font-size: 18px; font-weight: 700;'>{round(float(presicao * 100), 2)}</p>
                        </div>
                        <div style='background: #1e1e1e; border-radius: 8px; padding: 10px 14px;'>
                            <p style='margin: 0; font-size: 12px; color: #888;'>Recall</p>
                            <p style='margin: 4px 0 0; font-size: 18px; font-weight: 700;'>{round(float(recall * 100), 2)}</p>
                        </div>
                    </div>
                </div>
                """
            )

            st.html(
                f"""
                <div style='display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; margin-top: 25px'>
                    <div style='background: #1e1e1e; border-radius: 8px; padding: 6px 14px;'>
                        <p style='margin: 2px 0 0; font-size: 16px; font-weight: 700; line-height: 1.1; color:#990012;'>XGBoost</p>
                    </div>
                    <div style='background: #1e1e1e; border-radius: 8px; padding: 6px 10px;'>
                        <p style='margin: 2px 0 0; font-size: 16px; font-weight: 700; line-height: 1.1; color:#990012;'>{quali}</p>
                    </div>
                    <div style='background: #1e1e1e; border-radius: 8px; padding: 6px 10px;'>
                        <p style='margin: 2px 0 0; font-size: 16px; font-weight: 700; line-height: 1.1; color:#990012;'>Treino: 2018-{ano_atual}</p>
                    </div>
                </div>
                """
            )
        with col6:
            NOMES_PILOTOS = {
                "antonelli": "Andrea Kimi Antonelli",
                "norris": "Lando Norris",
                "hamilton": "Lewis Hamilton",
                "russell": "George Russell",
                "leclerc": "Charles Leclerc",
                "piastri": "Oscar Piastri",
                "max_verstappen": "Max Verstappen",
                "hadjar": "Isack Hadjar",
                "gasly": "Pierre Gasly",
                "lawson": "Liam Lawson",
                "colapinto": "Franco Colapinto",
                "arvid_lindblad": "Arvid Lindblad",
                "bottas": "Valtteri Bottas",
                "perez": "Sergio Pérez",
                "bortoleto": "Gabriel Bortoleto",
                "hulkenberg": "Nico Hülkenberg",
                "sainz": "Carlos Sainz",
                "alonso": "Fernando Alonso",
                "stroll": "Lance Stroll",
                "albon": "Alexander Albon",
                "ocon": "Esteban Ocon",
                "bearman": "Oliver Bearman",
            }

            predicoes = []
            for i in predicao.valores_pred:
                predicoes.append({
                    "id_piloto_atual": i["id_piloto_atual"],
                    "prob_podio": i["prob_podio"]
                })

            top = sorted(predicoes, key=lambda p: p["prob_podio"], reverse=True)[:10]
            top = top[::-1]

            nomes = [NOMES_PILOTOS.get(p["id_piloto_atual"], p["id_piloto_atual"].title()) for p in top]
            probs = [p["prob_podio"] * 100 for p in top]

            fig = go.Figure(go.Bar(
                x=probs,
                y=nomes,
                orientation="h",
                marker_color="#990012",
                text=[f"{p:.0f}%" for p in probs],
                textposition="outside",
                textfont=dict(color="#f2f2f2"),
            ))

            fig.update_layout(
                title=dict(text="Probabilidade de Pódio", font=dict(color="#f2f2f2", size=14), x=0),
                height=380,
                margin=dict(l=0, r=30, t=40, b=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                xaxis=dict(showgrid=False, range=[0, 100], showticklabels=False),
                yaxis=dict(showgrid=False),
            )

            st.plotly_chart(fig, use_container_width=True)