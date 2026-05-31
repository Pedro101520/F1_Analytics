Desenvolvi esse código que foi hospedado no GCP.

Basicamente é uma API RestFul que organiza as chamadas da API da Jolpica F1 e da um retorno estruturado, evitando a chamada multipla nas rotas.
Após o processamento e organização é salvo um arquivo json no google storage totalmente organizado, e esse é o que o dashboard vai consumir (Até o momento estou desenvolvendo a parte da página de pilotos)