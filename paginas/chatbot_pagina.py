import streamlit as st

from chatbot.chat_f1 import executa

def renderiza_chat():
    st.set_page_config(
        page_title="F1 ChatBot",
        page_icon=":checkered_flag:"
    )

    st.title("Fórmula 1 AI")

    if "historico" not in st.session_state:
        st.session_state.historico = []

    with st.sidebar:
        if st.button("Limpar a conversa", type="primary", use_container_width=True):
            st.session_state.historico = []
            st.rerun()

        if st.button("Voltar", use_container_width=True):
            st.session_state.page = "inicio"
            st.rerun()

    for mensagem in st.session_state.historico:
        with st.chat_message(mensagem["role"]):
            st.markdown(mensagem["content"])

    prompt = st.chat_input('Faça perguntas sobre a Fórmula 1')
    if prompt:
        prompt = prompt.replace('\n', ' \n')

        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.historico.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                try:
                    resultado = executa(prompt, st.session_state.historico)
                    categoria = resultado.get("categoria", "Não encontrei a categoria")
                    categoria = f"A categoria do chatbot selecionada para essa mensagem foi: {categoria}\n\n"
                    resposta = f"{categoria} {resultado.get('answer', 'Não consegui gerar uma resposta. Tente novamente.')}"
                except Exception as e:
                    resposta = f"Ocorreu um erro ao processar sua pergunta: {e}"

            st.markdown(resposta)

        st.session_state.historico.append({"role": "assistant", "content": resposta})
