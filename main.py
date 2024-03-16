from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import regex as re
from time import sleep

driver = webdriver.Chrome()

driver.get("https://portal.gupy.io/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="radix-0"]/div[2]/button'))
    )
finally:
    driver.find_element('xpath','//*[@id="radix-0"]/div[2]/button').click()

    driver.find_element('xpath','//*[@id="undefined-input"]').send_keys('Júnior')

    driver.find_element('xpath','//*[@id="undefined-button"]').click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[3]/div/div/aside/form/fieldset[1]/div[3]/label/div[2]'))
    )
finally:
    driver.find_element('xpath','//*[@id="__next"]/div[3]/div/div/aside/form/fieldset[1]/div[3]/label/div[2]').click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div/p/strong'))
    )
finally:
    total = driver.find_element('xpath','//*[@id="__next"]/div[2]/div/p/strong').get_property('textContent')

    vagas = driver.find_element('xpath','//*[@id="__next"]/div[3]/div/div/main/ul').get_property('childElementCount')

    total = re.findall("^\d{1,}",total)
    total = int(total[0])

    while vagas < total:
        scroll_origin = ScrollOrigin.from_viewport(10, 10)
        ActionChains(driver)\
            .scroll_from_origin(scroll_origin, 0, 200)\
            .perform()
        vagas = driver.find_element('xpath','//*[@id="__next"]/div[3]/div/div/main/ul').get_property('childElementCount')

    vagas = driver.find_element('xpath','//*[@id="__next"]/div[3]/div/div/main/ul')

    all_li = vagas.find_elements(By.TAG_NAME,'li')
    for li in all_li:
        print('Link: ',li.find_element(By.TAG_NAME,'a').get_property('href'))
        li = re.split('\n',li.text)
        print('Empresa: ',li[0])
        print('Posição: ',li[1])
        print('Local: ',li[2])
        print('Modelo: ',li[3])
        print('Contrato: ',li[4])
        print(li[5])
        if len(li) == 7:
            print(li[6])
        print('--------------------------------------------------------------')



    # print('Posição: ',li.find_element(By.TAG_NAME,'a').get_property('__reactProps$jdccrmqv3e')['children']['props']['data']['jobName'])
    # print('Empresa: ',li.find_element(By.TAG_NAME,'a').get_property('__reactProps$0tuklue9ikrd')['children']['props']['data']['careerPageName'])
    # print('Logo: ',li.find_element(By.TAG_NAME,'a').get_property('__reactProps$0tuklue9ikrd')['children']['props']['data']['careerPageUrlLogo'])
    # print('Descrição: ',li.find_element(By.TAG_NAME,'a').get_property('__reactProps$0tuklue9ikrd')['children']['props']['data']['description'])
    # print('Vaga: ',li.find_element(By.TAG_NAME,'a').get_property('__reactProps$0tuklue9ikrd')['children']['props']['data']['jobType'])
    # print('Publicação: ',li.find_element(By.TAG_NAME,'a').get_property('__reactProps$0tuklue9ikrd')['children']['props']['data']['publishedDate'])
    # print('Modelo: ',li.find_element(By.TAG_NAME,'a').get_property('__reactProps$0tuklue9ikrd')['children']['props']['data']['workplaceType'])