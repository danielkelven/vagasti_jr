import pandas as pd
from getVagas import BuscarVagas
import subprocess
import time
# Carrega as vagas
carregarVagas1 = BuscarVagas('Júnior')
lista1 = pd.DataFrame(carregarVagas1)
# Carrega as vagas
carregarVagas2 = BuscarVagas('Jr')
lista2 = pd.DataFrame(carregarVagas2)
listaCompleta = pd.concat([lista1, lista2],ignore_index=True)
# Exporta os dados gerados para Excel
listaCompleta.to_excel("ListaCompleta.xlsx",index=False)
# Palavras-chave para extrair os dados
termos = ['Service Now','Compliance','Quality Assurance','Informação','Software','Programador','Infraestrutura','SAP','Agile','Governança','Requisitos','Teste','QA','DevOps','Developer','Desenvolvedor','Suporte','Informática','Implantação','Front','Back','Cloud','Desenvolvimento','Redes','Sistema']
# Aplica o filtro das palavras chaves
vagasFiltradasDf = listaCompleta[listaCompleta['Cargo'].str.contains('|'.join(termos),case=False)]
# Exporta as vagas para o Excel
vagasFiltradasDf.to_excel("ListaFiltrada.xlsx",index=False)
# Especifica o caminho do arquivo Excel
caminhoArquivo = "ListaFiltrada.xlsx"
# Abre o arquivo no Excel
subprocess.Popen(['start',caminhoArquivo],shell=True).wait()
# Aguarda para fechar o arquivo
time.sleep(30000)