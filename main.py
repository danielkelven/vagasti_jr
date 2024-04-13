import pandas as pd
from getJobs import BuscarVagas
import subprocess
import time

def exeMain():
    # load the jobs
    loadJobs = BuscarVagas()
    loadedJobs = pd.DataFrame(loadJobs)

    # export the loaded jobs without filters
    loadedJobs.to_excel("listaCompleta.xlsx",index=False)

    # keywords to extract the main jobs
    keywords = ['Service Now','Compliance','Quality Assurance','Informação','Software','Programador','Infraestrutura','SAP','Agile','Governança','Requisitos','Teste','QA','DevOps','Developer','Desenvolvedor','Suporte','Informática','Implantação','Front','Back','Cloud','Desenvolvimento','Redes','Sistema']
    filteredDf = loadedJobs[loadedJobs['JobTitle'].str.contains('|'.join(keywords),case=False)]

    # export the loaded and filtered jobs
    filteredDf.to_excel("listaFiltrada.xlsx",index=False)
    
exeMain()

# specify the path to the file you want to open
filePath = "listaFiltrada.xlsx"

# open the file with its associated application and wait until it's closed
subprocess.Popen(['start', filePath], shell=True).wait()

time.sleep(30000)