import pandas as pd
from get_vagas import BuscarVagas

resultado = BuscarVagas('Júnior')

dados = pd.DataFrame(resultado)

# termos = ['Infraestrutura','Develop','Desenvolv','Suporte','Informática','Implantação','Front','Back','Cloud','Devops','Redes','Sistema']

# for row in dados.iterrows():
#     for termo in termos:

# dados.to_excel("dados_jr.xlsx")