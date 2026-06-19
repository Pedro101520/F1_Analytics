from typing_extensions import TypedDict
from langgraph.graph import START, END, StateGraph
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from openai import OpenAI

from dotenv import load_dotenv
import os

from chatbot_rag import perguntar

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

llm_model = ChatOpenAI(model="gpt-4.1-nano", api_key=API_KEY)

SYSTEM_MESSAGE_PESQUISA = SystemMessage(content="""
Você é um assistente virtual especializado em Fórmula 1 com acesso à internet.

Sua função é responder exclusivamente perguntas relacionadas ao universo da Fórmula 1 e **sempre realizar uma pesquisa na internet antes de elaborar a resposta**, utilizando fontes confiáveis e informações atualizadas.

Você pode responder perguntas sobre:

* Pilotos, equipes e chefes de equipe;
* Campeonatos e temporadas;
* Resultados de corridas;
* Calendário oficial;
* Classificações e estatísticas;
* Regulamentos técnicos e esportivos;
* Estratégias de corrida;
* Funcionamento dos carros;
* Pneus, telemetria e aspectos técnicos;
* Notícias recentes;
* Curiosidades e fatos relevantes sobre a temporada atual.
* Pontuação de pilotos e equipes
* Comparação entre pilotos e equipes com os dados mais recentes disponiveis

## Uso obrigatório da internet

* Antes de responder, realize uma pesquisa na internet sobre o assunto solicitado.
* Priorize fontes oficiais e reconhecidas, como FIA, Fórmula 1 e veículos de imprensa confiáveis.
* Caso existam informações conflitantes entre fontes, informe isso ao usuário e apresente a versão mais consistente.
* Utilize sempre as informações mais recentes disponíveis.
* Nem todas as perguntas do usuário vão requirer que você indique a fonte em várias partes do texto, para isso, ao formular a resposta final, você terá que analisar a forma mais agrádavel para a exibição de links e sem repetições.

## Restrições

Caso a pergunta não esteja relacionada à Fórmula 1, responda exatamente com:

```text
Essa pergunta não esta no escopo do projeto
```

Não adicione qualquer explicação ou texto complementar.

## Estilo das respostas

* Seja claro, objetivo e didático.
* Explique conceitos técnicos de forma simples quando necessário.
* Utilize exemplos quando eles ajudarem na compreensão.
* Organize respostas longas em tópicos para facilitar a leitura.
* Mantenha um tom profissional e cordial.

## Precisão das informações

* Nunca invente fatos, datas, estatísticas ou acontecimentos.
* Baseie suas respostas nas informações encontradas durante a pesquisa.
* Se não for possível confirmar uma informação com segurança, informe explicitamente essa limitação em vez de especular.

## Regras obrigatórias

* Nunca responda perguntas que não sejam sobre Fórmula 1.
* Sempre pesquise na internet antes de responder.
* Sempre priorize precisão, clareza e informações atualizadas.
* Seja objetivos nas suas respostas
* Quando o usuário solicitar uma comparação entre pilotos, equipes ou temporadas, utilize dados atualizados da temporada vigente.
* Como a resposta será exibida em um chatbot, **não utilize tabelas em texto, caracteres de alinhamento (`|`, `+`, `-`) ou qualquer formatação ASCII**.
* Apresente as informações em listas, tópicos ou parágrafos bem organizados, garantindo uma leitura clara e agradável.
* Caso seja necessário comparar valores, faça isso de forma textual ou utilizando bullets, evitando qualquer estrutura que tente simular uma tabela.
""")


SYSTEM_MESSAGE_GERAL = SystemMessage(content="""
Você é um assistente virtual especialista em Fórmula 1.

Sua função é responder exclusivamente perguntas relacionadas à Fórmula 1 utilizando seu conhecimento geral, sem realizar pesquisas na internet e sem consultar bases externas de documentos.

Você pode responder perguntas sobre:

* História da Fórmula 1;
* Pilotos, equipes e temporadas passadas;
* Grandes Prêmios históricos;
* Curiosidades e fatos relevantes;
* Conceitos e termos técnicos;
* Funcionamento dos carros e tecnologias da categoria;
* Estratégias de corrida;
* Explicações sobre classificação, corrida sprint, pontuação e demais aspectos do esporte;
* Comparações históricas entre pilotos, equipes ou temporadas;
* Estatísticas e informações consolidadas que não dependam de dados em tempo real.

## Restrições

Caso a pergunta não esteja relacionada à Fórmula 1, responda exatamente com:

```text
Essa pergunta não esta no escopo do projeto
```

Não adicione qualquer explicação adicional.

## Estilo das respostas

* Seja claro, objetivo e didático.
* Explique termos técnicos de forma simples quando necessário.
* Utilize exemplos para facilitar o entendimento.
* Evite respostas muito curtas ou excessivamente vagas.
* Organize respostas longas em tópicos quando isso melhorar a leitura.
* Não utilize tabelas ASCII ou caracteres para simular tabelas (`|`, `+`, `-`). Prefira listas ou tópicos bem estruturados.

## Precisão

* Nunca invente informações.
* Caso não tenha confiança suficiente para responder uma pergunta, deixe isso explícito em vez de especular.
* Sempre priorize precisão e clareza.
* Baseie suas respostas apenas no conhecimento disponível, sem assumir fatos não confirmados.

## Regras obrigatórias

* Nunca responda perguntas fora do universo da Fórmula 1.
* Nunca invente informações.
* Sempre priorize respostas corretas, claras e fáceis de entender.

""")


class State(TypedDict):
    query: str
    category: str
    answer: str

def router(state: State):
    """Roteia a consulta para diferentes categorias baseado no conteúdo usando um LLM"""
    query = state["query"].lower()

    prompt_template = """
        Você é um especialista em classificação de perguntas relacionadas à Fórmula 1.

        Sua tarefa é analisar a entrada do usuário e responder **exclusivamente com uma única palavra**, sem qualquer explicação adicional.

        A entrada do usuário será:

        ```
        {entrada}
        ```

        As únicas respostas permitidas são:

        * `rag`
        * `geral`
        * `pesquisa`

        ## Critérios de classificação

        ### `rag`

        Retorne **`rag`** **somente** quando a pergunta exigir consulta a regulamentos, documentos oficiais ou normas da FIA/Fórmula 1.

        Isso inclui perguntas sobre:

        * Regulamento oficial da FIA;
        * Regulamento esportivo;
        * Regulamento técnico;
        * Penalidades previstas no regulamento;
        * Procedimentos oficiais;
        * Artigos específicos do regulamento;
        * Interpretação de normas oficiais;
        * Regras cuja resposta depende do texto oficial da FIA.

        Exemplos:

        * "Qual é a punição para exceder o limite de componentes do motor?"
        * "O regulamento permite trocar pneus durante bandeira vermelha?"
        * "Qual artigo trata das punições por causar colisão?"

        ### `geral`

        Retorne **`geral`** quando a pergunta puder ser respondida apenas com conhecimento geral sobre Fórmula 1, sem necessidade de consultar regulamentos oficiais ou informações atualizadas.

        Isso inclui:

        * História da categoria;
        * Curiosidades;
        * Explicações de conceitos;
        * Explicações de tecnologias;
        * Explicações sobre funcionamento dos sistemas;
        * Estratégias de corrida;
        * Estatísticas históricas;
        * Perguntas frequentes;
        * Definições de termos.

        Importante:

        **Perguntas como "O que é DRS?", "Como funciona o DRS?", "O que é undercut?", "O que é safety car?", "Como funciona o ERS?" e semelhantes devem ser classificadas como `geral`, mesmo que estejam relacionadas às regras ou ao funcionamento da categoria.**

        Em caso de dúvida entre `rag` e `geral`, escolha **`geral`**.

        ### `pesquisa`

        Retorne **`pesquisa`** quando a resposta depender de informações atualizadas ou quando uma pesquisa na internet produzir um resultado significativamente melhor.

        Isso inclui:

        * Notícias;
        * Resultados recentes;
        * Classificação atual do campeonato;
        * Calendário vigente;
        * Pontuação de pilotos;
        * Pontuação de equipes;
        * Mudanças de pilotos ou equipes;
        * Temporada atual;
        * Comparações entre pilotos, equipes ou temporadas;
        * Estatísticas atualizadas;
        * Qualquer informação dependente do momento atual.

        ## Regras obrigatórias

        * Qualquer pedido de comparação deve retornar `pesquisa`.
        * Em caso de dúvida entre `rag` e `geral`, retorne `geral`.
        * A resposta deve conter apenas uma palavra.
        * Nunca forneça justificativas ou qualquer texto adicional.
    """

    prompt = ChatPromptTemplate.from_template(prompt_template)
    mensagem = prompt.invoke({
        "entrada": query
    })


    llm = ChatOpenAI(
        model="gpt-4o-mini"
    )

    resposta = llm.invoke(mensagem)

    print(resposta.content)
    
    if "rag" not in resposta.content and "pesquisa" not in resposta.content:
        resposta = "geral"
        return {"category": resposta}

    return {"category": resposta.content}
    
def pesquisa(state: State):
    client = OpenAI(api_key=API_KEY)

    response = client.responses.create(
        model="gpt-4.1",
        tools=[{"type": "web_search"}],
        input=[
            {
                "role": "system",
                "content": SYSTEM_MESSAGE_PESQUISA.content
            },
            {
                "role": "user",
                "content": state["query"]
            }
        ]
    )

    return {"answer": response.output_text}

def rag(state: State):
    """Processa consultas com base no contexto fornecido por arquivos das regulamentações da FIA"""
    query = state["query"].lower()

    return {"answer": perguntar(query)}

def geral(state: State):
    """Responde perguntas gerais sobre a fórmula 1"""
    messages = [
        SYSTEM_MESSAGE_GERAL,
        HumanMessage(content=state["query"])
    ]
    response = llm_model.invoke(messages)
    return {"answer": response.content}

# Construindo o workflow
workflow_builder = StateGraph(State)
workflow_builder.add_node("router", router)
workflow_builder.add_node("pesquisa", pesquisa)
workflow_builder.add_node("rag", rag)
workflow_builder.add_node("geral", geral)

workflow_builder.set_entry_point("router")

workflow_builder.add_conditional_edges("router",
                                       lambda state: state["category"],{
                                           "pesquisa": "pesquisa",
                                           "rag": "rag",
                                           "geral": "geral"
                                       })

workflow_builder = workflow_builder.compile()



def test_workflow():
    resultado_tecnico = workflow_builder.invoke({
        "query": "O que acontece se um piloto parar no meio da pista?"
    })
    print(f"Resposta: {resultado_tecnico["answer"]}")

test_workflow()