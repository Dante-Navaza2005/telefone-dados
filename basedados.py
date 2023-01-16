import pandas as pd
import plotly.express as px   

# Passo 1: Importaria a base de dados

tabela = pd.read_csv("telecom_users.csv")
asdasdaasdasd

#Passo 2: visualizar a base de dados

# -etender as informações que voce tem disponivel

#- Descobrir as cagadas da base de dados

tabela = tabela.drop("Unnamed: 0", axis = 1)                      


# Passo 3: Tratamento de Dados

#- resolver os valores que estao sendo reconhecidos de forma errada

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors  = "coerce")
#*transformar coluna total gasto de texto para numerico pois algum valor dentro nao é numerico


#*- resolver valores vazios*****

# colunas em que TODOS OS VALORES SAO VAZIOS VOU EXCLUIR

tabela = tabela.dropna(how = "all", axis = 1)


#linhas que tem PELO MENOS 1 valor vazio

tabela = tabela.dropna(how = "any", axis = 0)


# Passo 4: Analise Inicial

print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: analise detalhada - descobrir as causas do cancelamento dos clientes

# comparar cada coluna da base de dados com a coluna churn

# criar o grafico

#para cada coluna da minha tabela, eu quero criar um grafico

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x = coluna, color = "Churn", text_auto = True)
    #exibir o grafico                          
    grafico.show()

#*CONCLUSAO
    
#*clientes que tem familias maiores tendem a cancelar menos
    #promoções diferenciadas para mais pessoas da mesma familia

#* Os clientes nos primeiros meses tem uma tendencia MUITO maior a cancelar
    #pode ser algum marketing mt agressivo
    #pode ser que a experiencia nos primeiros meses seja ruim
    #posso fazer uma promoção no primeiro ano é mais barato

#*tem algum problema com o serviço de Fibra

#*Quanto mais serviços o cliente tem menos ele cancela
    #podemos oferecer mais serviços

#*Quase todos os cancelamentos tao no contrato mensal
    #oferecer planos de 2 anos

#* No boleto o cancelamento é muito maior
    #dar um desconto nas outras

print(tabela.info())
