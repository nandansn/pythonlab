import os

os.environ["PATH"] += os.pathsep + r'C:\Users\nrangasa.ORADEV\chromedriver\chromedriver_win32\chromedriver.exe'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time



driver = webdriver.Chrome('C:/Users/nrangasa.ORADEV/chromedriver/chromedriver_win32/chromedriver.exe')
driver.get("http://den01fqa.us.oracle.com:21323/dicloud/app/preparation")
driver.maximize_window()

def login():
    #login
    username = driver.find_element_by_name('j_username')
    username.send_keys('weblogic')
    password = driver.find_element_by_name('j_password')
    password.send_keys('welcome1')
    loginButton = driver.find_element_by_xpath('''//input[@name='action']''')
    loginButton.click()
    driver.set_page_load_timeout(20)


def create_name_dp():
    WebDriverWait(driver,40).until(EC.presence_of_element_located((By.XPATH,'''//input[@id='saveAndTransformTask']''')))
    WebDriverWait(driver,40).until(EC.presence_of_element_located((By.XPATH,'''//input[@id='name']''')))

    #create data prep
    dpName = driver.find_element_by_xpath('''//input[@id='name']''')
    dpName.send_keys('OCS to OCS')
    dpDescription = driver.find_element_by_xpath('''//textarea[@id='description']''')
    dpDescription.send_keys('Creating DP config....')

def create_source():
    # select source connection
    dpSourceConnection = driver.find_element_by_xpath('''//div[@id='oj-select-choice-srcConnection']''')
    dpSourceConnection.click()
    dpSourceConnectionSearch = driver.find_element_by_xpath('''//input[@type='text' and @title='Search field']''')
    dpSourceConnectionList = driver.find_element_by_xpath('''//div[@id='oj-listbox-drop']//ul[@id='oj-listbox-results-srcConnection']//li//div[@aria-label='OCS_CONN_DP_SRC']''')
    dpSourceConnectionList.click()
    # select source folder
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[@id='srcFolderPicker_launcher']''')))
    sourceFolderPicker = driver.find_element_by_xpath('''//button[@id='srcFolderPicker_launcher']''')
    sourceFolderPicker.click()
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[contains(@data-bind,'applyFileSel')]''')))
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//div[@id='srcFolderPicker_tree']/ul//li[@id='INSURANCE']''')))
    sourceFolder = driver.find_element_by_xpath('''//div[@id='srcFolderPicker_tree']/ul//li[@id='INSURANCE']/a/span[contains(text(),'INSURANCE')]''')
    sourceFolder.click()
    selectSourceFolder = driver.find_element_by_xpath('''//button[contains(@data-bind,'applyFileSel')]''')
    selectSourceFolder.click()

     # select source file
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[@id='srcFilePicker_launcher']''')))

    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'''//button[@id='srcFilePicker_launcher']''')))
    selectSourceFile = driver.find_element_by_xpath('''//button[@id='srcFilePicker_launcher']/div/span[contains(text(),'Select...')]''')
    selectSourceFile.click()

    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[contains(@data-bind,'applyFileSel')]''')))
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//div[@id='srcFilePicker_tree']/ul//li[@id='INSURANCE']''')))
    sourceFile = driver.find_element_by_xpath('''//div[@id='srcFilePicker_tree']/ul//li[@id='INSURANCE-40K.DAT']/a/span[contains(text(),'INSURANCE-40K.DAT')]''')
    sourceFile.click()
    selectSourceFile = driver.find_element_by_xpath('''//button[contains(@data-bind,'applyFileSel')]''')
    selectSourceFile.click()

def create_target():
    # select target connection
    dpTargetConnection = driver.find_element_by_xpath('''//div[@id='oj-select-choice-trgtConnection']''')
    dpTargetConnection.click()

    dpTargetConnectionSearch = driver.find_element_by_xpath('''//input[@type='text' and @title='Search field']''')
    dpTargetConnectionList = driver.find_element_by_xpath('''//div[@id='oj-listbox-drop']//ul[@id='oj-listbox-results-trgtConnection']//li//div[@aria-label='OCS_CONN_DP_TGT']''')
    dpTargetConnectionList.click()

    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[@id='trgtFolderPicker_launcher']''')))
    targetFolderPicker = driver.find_element_by_xpath('''//button[@id='trgtFolderPicker_launcher']''')
    targetFolderPicker.click()

    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[contains(@data-bind,'applyFileSel')]''')))
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//div[@id='trgtFolderPicker_tree']/ul//li[@id='INSURANCE']''')))
    targetFolder = driver.find_element_by_xpath('''//div[@id='trgtFolderPicker_tree']/ul//li[@id='INSURANCE']/a/span[contains(text(),'INSURANCE')]''')
    targetFolder.click()
    selectTargetFolder = driver.find_element_by_xpath('''//button[contains(@data-bind,'applyFileSel')]''')
    selectTargetFolder.click()

    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//input[@id='trgtFile']''')))
    targetFile = driver.find_element_by_xpath('''//input[@id='trgtFile']''')
    targetFile.send_keys('''OCS_TGT_FILE''')




time.sleep(10)


    
    

# save and run transform

# check the job status

driver.quit()

#driver.get("http://slc12mxs.us.oracle.com:18599/dicloud/login.html")




