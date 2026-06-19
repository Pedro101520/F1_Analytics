from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

CAMINHO_DB = "chatbot/db"

prompt_template = """
Você é um especialista em Fórmula 1.

Utilize APENAS as informações fornecidas na base de conhecimento para responder.

Pergunta do usuário:
{pergunta}

Base de conhecimento:
{base_conhecimento}

Instruções:
- Utilize linguagem simples, para que todos entendam
- Se o usuário te fizer uma pergunta generica e o contexto fornecido não responder com exatidão, explique para o usuário o motivo de não conseguir responder, levando em consideração o que você obtiver de contexto
- Responda sempre em português.
- Seja claro e objetivo.
- Se o usuário pedir uma opnião, como por exemplo: "qual a norma mais rígida". Acesse o contexto e o seu conhecimento e dê um retorno para ele
- Quando fizer sentido, organize a resposta em tópicos.
- Não invente informações que não estejam na base de conhecimento.
- Se a base não contiver informações suficientes para responder, diga:

Caso não enconntre a resposta no contexto, diga que em sua base de conhecimento não tem as informações solicitadas

Resposta:
"""

def perguntar(mensagem_usuario):
    funcao_embedding = OpenAIEmbeddings()
    db = Chroma(persist_directory=CAMINHO_DB, embedding_function=funcao_embedding)

    resultados = db.similarity_search_with_relevance_scores(mensagem_usuario, k=5)


    if len(resultados) == 0:
        print("Não consegui encontrar alguma informação relevante na base")
        return
    
    textos_resultado = []
    for resultado in resultados:
        texto = resultado[0].page_content
        textos_resultado.append(texto)
    
    base_conhecimento = "\n\n----\n\n".join(textos_resultado)
    prompt = ChatPromptTemplate.from_template(prompt_template)
    mensagem = prompt.invoke({
        "pergunta": mensagem_usuario,
        "base_conhecimento": base_conhecimento
    })

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2
    )

    resposta = llm.invoke(mensagem)

    return resposta.content