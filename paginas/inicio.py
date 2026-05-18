import streamlit as st

def pagina_inicial():
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        container = st.container(border=True)
        container.write("This is inside the container")
    with col2:
        container = st.container(border=True)
        container.write("This is inside the container")
    with col3:
        container = st.container(border=True)
        container.write("This is inside the container")
    with col4:
        container = st.container(border=True)
        container.write("This is inside the container")

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