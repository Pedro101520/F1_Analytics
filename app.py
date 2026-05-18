import streamlit as st
import requests

from paginas.inicio import pagina_inicial
from paginas.pilotos import info_pilotos

# valor = requests.get("https://api.jolpi.ca/ergast/f1/2024/driverstandings/").json()
# print(valor)

def wide_mode():
    st.set_page_config(layout="wide")
wide_mode()

if "page" not in st.session_state:
    st.session_state.page = "inicio"

col1, col2, col3, col4, col5 = st.columns([5,1,1,1,1])

with col1:
    img_col, text_col = st.columns([1, 10])
    with img_col:
        st.image("assets/F1+Logo.png", width=50)
    with text_col:
        st.write("##### F1 Analytics - Temporada 2025")
with col2:
    if st.button("Inicio", use_container_width=True):
        st.session_state.page = "inicio"
        st.rerun()
with col3:
    if st.button("Pilotos", use_container_width=True):
        st.session_state.page = "pilotos"
        st.rerun()
with col4:
    st.button("Pedro223", use_container_width=True)
with col5:
    st.button("Pedro298", use_container_width=True)


st.space()
st.space()


if st.session_state.page == "inicio":
    pagina_inicial()
elif st.session_state.page == "pilotos":
    info_pilotos()