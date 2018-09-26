import os


os.environ["PATH"] += os.pathsep + r'C:\Users\nrangasa.ORADEV\chromedriver\chromedriver_win32\chromedriver.exe'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import *

import time

host ='slc12mjj.us.oracle.com'
port ='21506'

url = "http://host:port/dicloud/app/preparation"

url = url.replace('host',host).replace('port',port)
 
print(url)

driver = webdriver.Chrome('C:/Users/nrangasa.ORADEV/chromedriver/chromedriver_win32/chromedriver.exe')
driver.get(url)
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
    dpSourceConnectionList = driver.find_element_by_xpath('''//div[@id='oj-listbox-drop']//ul[@id='oj-listbox-results-srcConnection']//li//div[@aria-label='OCS_SRC_CON']''')
    dpSourceConnectionList.click()
    # select source folder
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[@id='srcFolderPicker_launcher']''')))
    sourceFolderPicker = driver.find_element_by_xpath('''//button[@id='srcFolderPicker_launcher']''')
    sourceFolderPicker.click()
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[contains(@data-bind,'applyFileSel')]''')))
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//div[@id='srcFolderPicker_tree']/ul//li[@id='OCSDPTGT']''')))
    sourceFolder = driver.find_element_by_xpath('''//div[@id='srcFolderPicker_tree']/ul//li[@id='OCSDPTGT']/a/span[contains(text(),'OCSDPTGT')]''')
    sourceFolder.click()
    selectSourceFolder = driver.find_element_by_xpath('''//button[contains(@data-bind,'applyFileSel')]''')
    selectSourceFolder.click()

     # select source file
    ActionChains(driver).send_keys(Keys.PAGE_DOWN)
    ActionChains(driver).send_keys(Keys.PAGE_DOWN)
    ActionChains(driver).send_keys(Keys.PAGE_DOWN)
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[@id='srcFilePicker_launcher']''')))

    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'''//button[@id='srcFilePicker_launcher']''')))
    selectSourceFile = driver.find_element_by_xpath('''//button[@id='srcFilePicker_launcher']''')
    time.sleep(10)
    ActionChains(driver).move_to_element(selectSourceFile).click(selectSourceFile).perform()
    

    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[contains(@data-bind,'applyFileSel')]''')))
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//div[@id='srcFilePicker_tree']/ul//li[@id='test_data_user_details.txt']''')))
    sourceFile = driver.find_element_by_xpath('''//div[@id='srcFilePicker_tree']/ul//li[@id='test_data_user_details.txt']/a/span[contains(text(),'test_data_user_details.txt')]''')
    sourceFile.click()
    selectSourceFile = driver.find_element_by_xpath('''//button[contains(@data-bind,'applyFileSel')]''')
    selectSourceFile.click()

    time.sleep(10)

def create_target():
    # select target connection
    dpTargetConnection = driver.find_element_by_xpath('''//div[@id='oj-select-choice-trgtConnection']''')
    dpTargetConnection.click()

    dpTargetConnectionSearch = driver.find_element_by_xpath('''//input[@type='text' and @title='Search field']''')
    dpTargetConnectionList = driver.find_element_by_xpath('''//div[@id='oj-listbox-drop']//ul[@id='oj-listbox-results-trgtConnection']//li//div[@aria-label='OCS_TGT_CON']''')
    dpTargetConnectionList.click()

    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[@id='trgtFolderPicker_launcher']''')))
    targetFolderPicker = driver.find_element_by_xpath('''//button[@id='trgtFolderPicker_launcher']''')
    targetFolderPicker.click()

    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//button[contains(@data-bind,'applyFileSel')]''')))
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//div[@id='trgtFolderPicker_tree']/ul//li[@id='OCSDPTGT']''')))
    targetFolder = driver.find_element_by_xpath('''//div[@id='trgtFolderPicker_tree']/ul//li[@id='OCSDPTGT']/a/span[contains(text(),'OCSDPTGT')]''')
    targetFolder.click()
    selectTargetFolder = driver.find_element_by_xpath('''//button[contains(@data-bind,'applyFileSel')]''')
    selectTargetFolder.click()
    time.sleep(10)
    WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,'''//input[@id='trgtFile']''')))
    targetFile = driver.find_element_by_id('trgtFile')

    targetFile.send_keys('''OCS_TGT_DATA''')

def save_and_transform():
    driver.find_element_by_xpath("//input[@id='saveAndTransformTask']").click()
    time.sleep(10)

def save_and_run():
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'''//div[@data-id='column']''')))
    WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,'''//div[@data-id='sample']''')))
    WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'''//input[@id='runTask']''')))
    driver.find_element_by_xpath("//input[@id='runTask']").click()
    time.sleep(60)



login()
create_name_dp()
create_source()
create_target()
save_and_transform()
save_and_run()

driver.quit()


    
    

# save and run transform

# check the job status



#driver.get("http://slc12mxs.us.oracle.com:18599/dicloud/login.html")




