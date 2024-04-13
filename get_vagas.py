from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import regex as re
import pandas as pd

# function to get all jobs in gupy
def BuscarVagas():
    # browser parameters
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://portal.gupy.io/")

    # wait the pop-up button
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="radix-0"]/div[2]/button'))
        )
    finally:
        # click in the pop-up button
        browser.find_element(By.XPATH,'//*[@id="radix-0"]/div[2]/button').click()
        # press the search parameters
        browser.find_element(By.XPATH,'//*[@id="undefined-input"]').send_keys('Júnior')
        # execute the search
        browser.find_element(By.XPATH,'//*[@id="undefined-button"]').click()

    # wait the checkbox of remote jobs filter
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[3]/div/div/aside/form/fieldset[1]/div[3]/label/div[2]'))
        )
    finally:
        # check the remote jobs filter
        browser.find_element(By.XPATH,'//*[@id="__next"]/div[3]/div/div/aside/form/fieldset[1]/div[3]/label/div[2]').click()

    # wait the return of all jobs in the filter
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="__next"]/div[2]/div/p/strong'))
        )
    finally:
        # define the return of all jobs in the filter
        def allJobs():
            listJobs = browser.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/p/strong').get_property('textContent')
            listJobs = re.findall("^\d{1,}",listJobs)
            counter = int(listJobs[0])
            return counter
    
    # wait the return of jobs loaded  
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/ul'))
        )
    finally:
        # define the return of jobs loaded
        def loadJobs():
            count = browser.find_element(By.XPATH,'//*[@id="main-content"]/ul').get_property('childElementCount')
            return count

        # this function execute the 'CTRL+END' command
        while loadJobs() < allJobs():
            ActionChains(browser)\
                .key_down(Keys.CONTROL)\
                .key_down(Keys.END)\
                .perform()

        # this parameters creates the array with individual data of jobs
        gridJobs = browser.find_element(By.XPATH,'//*[@id="main-content"]/ul')
        jobs = gridJobs.find_elements(By.XPATH,'//*[@id="main-content"]/ul/li')
        baseArray = []
        
        # this loop appends the links of jobs in the array
        for i in jobs:
            jobUrl = str(i.find_element(By.TAG_NAME,'a').get_property('href'))
            job = i.text.split('\n')
            if len(job) == 7:
                job.append(jobUrl)
            else:
                job.insert(5,'Não informado')
                job.append(jobUrl)
            baseArray.append(job)
        
        # this part prepares the dataframe to excel export
        jobsDf = pd.DataFrame(baseArray, columns=['JobOrganization','JobTitle','JobPlace','JobWorkplace','JobType','Acessibility','Publish','JobURL'])
        jobsDf['Publish'] = jobsDf['Publish'].astype(str).str.replace('Publicada em: ', '', regex = False)
        jobsDf['Publish'] = pd.to_datetime(jobsDf['Publish'],format='%d/%m/%Y')
        
        # define the parameters to filter the jobs between the current and the previous month 
        currentYear = datetime.now().year
        currentMonth = datetime.now().month
        previousYear = currentYear if currentMonth != 1 else currentYear - 1
        previousMonth = currentMonth - 1 if currentMonth != 1 else 12
        
        # execute the filter
        filteredDf = jobsDf[((jobsDf['Publish'].dt.year == currentYear) & (jobsDf['Publish'].dt.month == currentMonth)) |
                        ((jobsDf['Publish'].dt.year == previousYear) & (jobsDf['Publish'].dt.month == previousMonth))]
        
        return filteredDf