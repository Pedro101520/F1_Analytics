# F1 Analytics Dashboard

🔗 **Dashboard:** https://formula1-analytics-project.streamlit.app

📦 **Repositório do ETL:** https://github.com/Pedro101520/API_ETL_F1

📦 **Repositório do modelo de predição:** https://github.com/Pedro101520/f1_prediction_models

---

Este projeto é um dashboard interativo sobre informações da Fórmula 1, com dados extraídos da API Jolpica F1 e da biblioteca FastF1. O desenvolvimento foi feito com Streamlit, que consome dados pré-processados e salvos em um storage do Google Cloud após etapas de ETL.

O projeto também conta com um modelo preditivo feito com XGBoost (usando a função `XGBClassifier`) e um chatbot 4 em 1 feito com LangChain e LangGraph, onde o chatbot conta com as seguintes funções:

- **Pesquisa na internet**
- **RAG** para consultas nas normas da FIA
- **Especialista no dashboard**, que explica o significado de cada campo do dashboard
- **Especialista em respostas gerais sobre F1**, que responde desde curiosidades até momentos históricos da Fórmula 1

---

## Tecnologias utilizadas

- Python
- Pandas
- Plotly
- Google Cloud (Storage, Scheduler, Cloud Run)
- Docker
- Streamlit
- OpenAI
- ChromaDB
- LangChain
- LangGraph
- BeautifulSoup
- API Jolpica F1
- FastF1
- API Open-Meteo
- APIs que desenvolvi: API ETL, API Predição (repositórios listados no início da documentação)

---

## Diagrama da arquitetura
<img width="789" height="752" alt="image" src="https://github.com/user-attachments/assets/5e3562f4-aeb8-4209-a2af-a7295ff84d23" />


## Como funciona

### Página Início

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/962b195b-03de-417d-8cad-7eb111013561"/>

Inclui informações atuais do campeonato, como a quantidade de rodadas restantes, onde será a próxima corrida e quem ganhou a última corrida disputada. Também é possível ver informações sobre como estará o clima no próximo GP.

Destaco aqui o campo de notícias, para o qual desenvolvi um script usando BeautifulSoup para a coleta de notícias no site Motorsport.

Também temos informações sobre o próximo circuito e um calendário com as próximas corridas.

### Página de Pilotos

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/cd6aadfe-538f-42dc-a419-9dab70637e55"/>

A página de pilotos permite selecionar um piloto específico para ver o desempenho individual dele na temporada atual. Essas informações incluem: nome, equipe, estreia, posição no campeonato, quantidade de pontos, vitórias, pódios, pole positions, melhor resultado de corrida, média de largada (média de posição de grid) e corridas não concluídas (inclui corridas não iniciadas e corridas abandonadas).

Também é possível ver um gráfico feito com Plotly, que mostra a evolução da quantidade de pontos e a posição final em cada corrida.

Inclui também uma tabela onde o usuário pode selecionar outro piloto para ter uma comparação de desempenho entre pilotos.

Por fim, uma tabela indica os resultados do piloto em cada GP.

### Equipes

<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/1e90b2b7-175c-4e07-ac09-1a3b8324e411"/>

Aqui o usuário pode selecionar uma equipe específica para ver informações de desempenho, como: posição no campeonato, pontuação, vitórias, pódios, pole positions, melhor resultado (indicado pelo melhor resultado entre os pilotos titulares) e quantidade de abandonos.

Também inclui um gráfico para mostrar o desempenho da equipe por posição e pontos, destacando que aqui é exibida a pontuação agregada por GP.

Adicionei também um campo de comparação, onde o usuário pode selecionar outra equipe para ter uma comparação.

Por fim, um campo mostra como está o duelo interno entre os pilotos titulares da equipe, exibindo informações de pódios, melhores resultados, média de largada e pontos médios por GP.

### Campeonato

Aqui exibo uma tabela e um gráfico para pilotos e equipes, representando a classificação geral no campeonato mundial.

Adicionei um campo que mostra quem está no pódio, seja piloto ou equipe.

Por fim, o campo de predição de pódio exibe métricas de desempenho: acurácia, F1-Score, precisão e recall.

Destaco aqui que desenvolvi dois modelos: um com dados antes da qualifying e outro com dados depois.

Inclui também um gráfico que mostra a probabilidade de cada piloto ir ao pódio.

Para mais detalhes, acesse o repositório da API do modelo de predição que desenvolvi: https://github.com/Pedro101520/f1_prediction_models — lá constam mais detalhes sobre o desenvolvimento e as métricas.

### ChatBot F1
<img width="700" height="500" alt="image" src="https://github.com/user-attachments/assets/267ebc7e-a736-47fe-9d97-20dc146a14f1"/>

Feito com LangChain e LangGraph, desenvolvi um chatbot 4 em 1 baseado em um workflow de IA para explicar diferentes aspectos da Fórmula 1 de forma didática, contando com os seguintes módulos:

Pesquisador: o modelo tem acesso à internet e pode pesquisar desde as últimas notícias até a tabela de pontuação mais atual
Geral: programado para responder a perguntas gerais, como curiosidades e momentos históricos
RAG: inclui toda a regulamentação da FIA, onde o modelo consegue explicar qualquer ponto dela de forma bem didática
Especialista no dashboard: responsável por explicar cada campo do dashboard com clareza
- **Pesquisador:** o modelo tem acesso à internet e pode pesquisar desde as últimas notícias até a tabela de pontuação mais atual
- **Geral:** programado para responder a perguntas gerais, como curiosidades e momentos históricos
- **RAG:** inclui toda a regulamentação da FIA, onde o modelo consegue explicar qualquer ponto dela de forma bem didática
- **Especialista no dashboard:** responsável por explicar cada campo do dashboard com clareza
