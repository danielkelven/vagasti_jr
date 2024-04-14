from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import regex as re
import pandas as pd
# Função para pesquisar as vagas
def BuscarVagas(termoPesquisa):
    # Parâmetros do navegador
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    navegador.get('https://portal.gupy.io/')
    # Aguardar a exibição do pop-up
    try:
        element = WebDriverWait(navegador, 20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="radix-0"]/div[2]/button'))
        )
    finally:
        # Clicar no botão do pop-up
        navegador.find_element(By.XPATH,'//*[@id="radix-0"]/div[2]/button').click()
        # Preencher o termo da pesquisa
        navegador.find_element(By.XPATH,'//*[@id="undefined-input"]').send_keys(termoPesquisa)
        # Executa a busca
        navegador.find_element(By.XPATH,'//*[@id="undefined-button"]').click()
    # Aguarda a página carregar
    try:
        element = WebDriverWait(navegador, 20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[3]/div/div/aside/form/fieldset[1]/div[3]/label/div[2]'))
        )
    finally:
        # Clica no filtro para vagas remotas
        navegador.find_element(By.XPATH,'//*[@id="__next"]/div[3]/div/div/aside/form/fieldset[1]/div[3]/label/div[2]').click()
    # Aguarda o total de vagas filtradas
    try:
        element = WebDriverWait(navegador, 20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[2]/div/p/strong'))
        )
    finally:
        # Função para contar o total de vagas filtradas
        def totalVagas():
            listaVagas = navegador.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/p/strong').get_property('textContent')
            listaVagas = re.findall("^\d{1,}",listaVagas)
            contador = int(listaVagas[0])
            return contador
    # Aguarda o total de vagas carregadas
    try:
        element = WebDriverWait(navegador, 20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="main-content"]/ul'))
        )
    finally:
        # Função para contar as vagas carregadas
        def vagasCarregadas():
            count = navegador.find_element(By.XPATH,'//*[@id="main-content"]/ul').get_property('childElementCount')
            return count
        # Executa o comando 'CTRL+END'
        while vagasCarregadas() < totalVagas():
            ActionChains(navegador)\
                .key_down(Keys.CONTROL)\
                .key_down(Keys.END)\
                .perform()
        # Cria uma lista de vagas
        gridVagas = navegador.find_element(By.XPATH,'//*[@id="main-content"]/ul')
        # Extrai a lista de vagas
        vagas = gridVagas.find_elements(By.XPATH,'//*[@id="main-content"]/ul/li')
        arrayVagas = []
        # Esse loop insere o link das vagas na lista
        for i in vagas:
            jobUrl = str(i.find_element(By.TAG_NAME,'a').get_property('href'))
            job = i.text.split('\n')
            if len(job) == 7:
                job.append(jobUrl)
            else:
                job.insert(5,'Não informado')
                job.append(jobUrl)
            arrayVagas.append(job)
        # Cria os filtros e as colunas do dataframe que contém as vagas
        vagasDf = pd.DataFrame(arrayVagas, columns=['Empresa','Cargo','Local','Método','Tipo','Acessibilidade','Publicação','Link'])
        vagasDf['Publicação'] = vagasDf['Publicação'].astype(str).str.replace('Publicada em: ','',regex=False)
        vagasDf['Publicação'] = pd.to_datetime(vagasDf['Publicação'],format='%d/%m/%Y')
        # Define os parâmetros de tempo de vaga
        anoAtual = datetime.now().year
        mesAtual = datetime.now().month
        anoAnterior = anoAtual if mesAtual != 1 else anoAtual - 1
        mesAnterior = mesAtual - 1 if mesAtual != 1 else 12
        # Executa o filtro
        vagasFiltradasDf = vagasDf[((vagasDf['Publicação'].dt.year == anoAtual) & (vagasDf['Publicação'].dt.month == mesAtual)) |
                        ((vagasDf['Publicação'].dt.year == anoAnterior) & (vagasDf['Publicação'].dt.month == mesAnterior))]
        # Retorna os dados
        return vagasFiltradasDf