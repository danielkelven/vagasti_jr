from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import regex as re
import pandas as pd

def BuscarVagas(palavraChave:str):
    browser = webdriver.Chrome()
    
    browser.maximize_window()

    browser.get("https://portal.gupy.io/")

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="radix-0"]/div[2]/button'))
        )
    finally:
        browser.find_element(By.XPATH,'//*[@id="radix-0"]/div[2]/button').click()

        browser.find_element(By.XPATH,'//*[@id="undefined-input"]').send_keys(palavraChave)

        browser.find_element(By.XPATH,'//*[@id="undefined-button"]').click()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[3]/div/div/aside/form/fieldset[1]/div[3]/label/div[2]'))
        )
    finally:
        browser.find_element(By.XPATH,'//*[@id="__next"]/div[3]/div/div/aside/form/fieldset[1]/div[3]/label/div[2]').click()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[2]/div/p/strong'))
        )
    finally:
        def totalVagas():
            listVagas = browser.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/p/strong').get_property('textContent')
            listVagas = re.findall("^\d{1,}",listVagas)
            count = int(listVagas[0])
            return count
        
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/ul'))
        )
    finally:
        def vagasCarregadas():
            count = browser.find_element(By.XPATH,'//*[@id="main-content"]/ul').get_property('childElementCount')
            return count

        while vagasCarregadas() < totalVagas():
            ActionChains(browser)\
                .key_down(Keys.CONTROL)\
                .key_down(Keys.END)\
                .perform()

        gridVagas = browser.find_element(By.XPATH,'//*[@id="main-content"]/ul')

        vagas = gridVagas.find_elements(By.XPATH,'//*[@id="main-content"]/ul/li')

        baseArray = []

        for i in vagas:
            link = str(i.find_element(By.TAG_NAME,'a').get_property('href'))
            vaga = i.text.split('\n')
            if len(vaga) == 7:
                vaga.append(link)
            else:
                vaga.insert(5,"Não informado")
                vaga.append(link)
            baseArray.append(vaga)
        
        dfGeral = pd.DataFrame(baseArray, columns=['Empresa', 'Cargo', 'Local', 'Modalidade', 'Tipo', 'Acessivel', 'Publicacao', 'Link'])

        return dfGeral