from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import regex as re
import pandas as pd
import ast

def BuscarVagas(palavraChave:str):
    browser = webdriver.Chrome()

    browser.get("https://portal.gupy.io/")

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="radix-0"]/div[2]/button'))
        )
    finally:
        browser.find_element('xpath','//*[@id="radix-0"]/div[2]/button').click()

        browser.find_element('xpath','//*[@id="undefined-input"]').send_keys(palavraChave)

        browser.find_element('xpath','//*[@id="undefined-button"]').click()

    # try:
    #     element = WebDriverWait(browser, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[3]/div/div/aside/form/fieldset[1]/div[3]/label/div[2]'))
    #     )
    # finally:
    #     browser.find_element('xpath','//*[@id="__next"]/div[3]/div/div/aside/form/fieldset[1]/div[3]/label/div[2]').click()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/p/strong'))
        )
    finally:
        totalVagas = browser.find_element('xpath','//*[@id="__next"]/div[2]/div/p/strong').get_property('textContent')

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[3]/div/div/main/ul'))
        )
    finally:
        vagasCarregadas = browser.find_element('xpath','//*[@id="__next"]/div[3]/div/div/main/ul').get_property('childElementCount')

        totalVagas = re.findall("^\d{1,}",totalVagas)
        totalVagas = int(totalVagas[0])

        while vagasCarregadas < totalVagas:
            scroll_origin = ScrollOrigin.from_viewport(10, 10)
            ActionChains(browser)\
                .scroll_from_origin(scroll_origin, 0, 200)\
                .perform()
            vagasCarregadas = browser.find_element('xpath','//*[@id="__next"]/div[3]/div/div/main/ul').get_property('childElementCount')

        gridVagas = browser.find_element('xpath','//*[@id="__next"]/div[3]/div/div/main/ul')

        vagas = gridVagas.find_elements(By.TAG_NAME,'li')
        
        strArray = ''

        for vaga in vagas:
            dadosVaga = re.split('\n',vaga.text)
            if len(dadosVaga) == 7:
                if strArray == '':
                    strArray = "['" + str(dadosVaga).replace("\n",",'") + ",'" + str(vaga.find_element(By.TAG_NAME,'a').get_property('href')) + "']\n"
                else:
                    strArray = strArray + "\n['" + str(dadosVaga).replace("\n","','") + ",'" + str(vaga.find_element(By.TAG_NAME,'a').get_property('href')) + "']"
            else:
                if strArray == '':
                    strArray = "['" + str(dadosVaga).replace("\n",",'") + ",'Não informado'," + ",'" + str(vaga.find_element(By.TAG_NAME,'a').get_property('href')) + "']\n"
                else:
                    strArray = strArray + "\n['" + str(dadosVaga).replace("\n","','") + ",'Não informado'," + ",'" + str(vaga.find_element(By.TAG_NAME,'a').get_property('href')) + "']"
        
        strArray = strArray.replace("['['","['")
        strArray = strArray.replace("'],'https","','https")
        strArray = strArray.replace("\n\n","\n")

        baseArray = [ast.literal_eval(linha) for linha in strArray.split('\n')]
        
        dfGeral = pd.DataFrame(baseArray, columns=['Empresa', 'Cargo', 'Local', 'Modalidade', 'Tipo de Vaga', 'Acessível para PCD', 'Publicada em', 'Link'])

        return dfGeral