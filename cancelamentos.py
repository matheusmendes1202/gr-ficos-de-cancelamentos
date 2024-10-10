import pandas as pd
from IPython.core.display_functions import display

#importar base de dados
tabela = pd.read_csv("cancelamentos_sample.csv")
print(tabela)
#entender as informações que eu tenho disponivel
#procurar os cagadas da base de dados
#colunas inuteis que nao tem ajudar = te atrapalham

tabela = tabela.dropna() # jogar fora informação vazia
display(tabela.info())

#analise de cancelamento
display(tabela["cancelou"].value_counts(normalize=True))
#analise de percentual = normalizado (estatistica)
#56% cancelaram
#43% não cancelaram
#analise de causa de cancelamento de clientes
import plotly.express as px
#criar grafico
#para da coluna na tabela criar um grafico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna,color="cancelou", text_auto=True)
    #causa de cancelamento todos os clientes de contrato mensal cancelaram
    #exibir grafico
    grafico.show()
    #grafico certo é o grafico simples

    #duração do contrato nao pode ser mensal

    tabela = tabela[tabela["duracao_contrato"]!= "monthyl"]

#atrasos so podem ser ate 20 dias
    tabela= tabela[tabela["dias_atraso"]<=20]

    #ligaçoes de call center
    tabela = tabela[tabela["ligacoes_callcenter"]<=4]





