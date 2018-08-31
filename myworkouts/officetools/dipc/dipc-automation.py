from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def init_app_in_chrome():
    chromeDriver = webdriver.Chrome('''C:/Users/nrangasa.ORADEV/chromedriver/chromedriver_win32/chromedriver.exe''')
    chromeDriver.get('''http://slc14vqd.us.oracle.com:16094/dicloud''')
    return chromeDriver


def dipc_login(chromeDriver):
    userNameTxtBox = chromeDriver.find_element_by_xpath('''//input[@id='j_username']''')
    userNameTxtBox.clear()
    userNameTxtBox.send_keys('weblogic')

    userPwdTxtBox = chromeDriver.find_element_by_xpath('''//input[@id='j_password']''')
    userPwdTxtBox.clear()
    userPwdTxtBox.send_keys('welcome1')

    chromeDriver.find_element_by_xpath('''//input[@name='action']''').click()
    try:
       elementPresent = EC.presence_of_element_located((By.XPATH,'''//div[@id='obj-metric-preview']/div/div[5]/a/h2'''))
       WebDriverWait(chromeDriver,20).until(elementPresent)
       if chromeDriver.find_element_by_xpath('''//div[@id='obj-metric-preview']/div/div[5]/a/h2''').is_displayed() :
           print("Home page has been successfully displayed")
    except TimeoutException as toe:
        print('''Element not found. Timed out'''+toe.with_traceback())

def open_catalog(chromeDriver):
    chromeDriver.find_element_by_xpath('''//li[@id="catalog"]/a[@id="opaas-letfnav-item-catalog"]//span[@id="opaas-letfnav-item-text-catalog"]''').click()
    try:
        elementPresent = EC.presence_of_all_elements_located((By.XPATH,'''//div/button[@id="createButton"]/div/span[contains(text(),'Create')]'''))    
        WebDriverWait(chromeDriver,20).until(elementPresent)
        
    except TimeoutException as toe:
        print('''Element not found. Timed out'''+toe.with_traceback())

def open_dp(chromedriver):
    if chromeDriver.find_element_by_xpath('''//div/button[@id="createButton"]/div/span[contains(text(),'Create')]''').is_displayed() :
            chromeDriver.find_element_by_xpath('''//div/button[@id="createButton"]/div/span[contains(text(),'Create')]''').click()
            chromeDriver.find_element_by_xpath('''//div[@id="actionMenu_layer"]/ul[@id="actionMenu"]//li[@id="Data Preparation"]/a[@href="Data Preparation"]''').click()
    

def close_app(chromeDriver):
    chromeDriver.close()

chromeDriver = init_app_in_chrome()
dipc_login(chromeDriver)
open_catalog(chromeDriver)
open_dp(chromeDriver)
close_app(chromeDriver)



