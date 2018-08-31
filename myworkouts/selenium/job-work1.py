from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

#Opening the application
driver =  webdriver.Chrome('C:\\Users\\nrangasa.ORADEV\\chromedriver\\chromedriver_win32\\chromedriver.exe')
driver.get('https://dms.stjude.org/DMS/webui/webshellpage.aspx?databasename=DMS')
userNameTextBoxElement =  driver.find_element_by_name('user_name')
pwdTextBoxElelemnt = driver.find_element_by_name('password')

#Login to the application
userNameTextBoxElement.clear()
userNameTextBoxElement.send_keys('dmsneustar')
pwdTextBoxElelemnt.clear()
pwdTextBoxElelemnt.send_keys('DMSpocpw2015n')
loginButton = driver.find_element_by_xpath('//*[@id="form1"]/p/button')
loginButton.click()



#Getting into home page
time.sleep(20)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Home')]''').text)

#Opening Constituents page.
driver.find_element_by_xpath('''//button[contains(text(),'Constituents')]''').click()
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Constituents')]''').text)

#Marketing Communications
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Marketing and Communications')]''').click()
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Marketing and Communications')]''').text)

#Major Giving
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Major Giving')]''').click()
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Major Giving')]''').text)

#Revenue
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Revenue')]''').click()
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Revenue')]''').text)

#Events
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Revenue')]''').click()
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Revenue')]''').text)

#Membership programs
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Membership')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Membership programs')]''').text)

#Prospects
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Prospects')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Prospects')]''').text)

#Volunteers
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Volunteers')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Volunteers')]''').text)

#Foundations
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Foundations')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Foundations')]''').text)

#Sponsorship
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Sponsorship')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Sponsorship')]''').text)

driver.maximize_window()

#Fundraising
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Fundraising')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Fundraising')]''').text)

#Treasury
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Treasury')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Treasury')]''').text)

#Web
time.sleep(5)
driver.find_element_by_xpath('''//button[contains(text(),'Web')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Web')]''').text)

#Click the icon
driver.find_element_by_xpath('''//button[@class=' x-btn-text x-toolbar-more-icon']''').click()
time.sleep(1)

driver.find_element_by_xpath('''//a/span[contains(text(),'Reports')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Reports')]''').text)

driver.find_element_by_xpath('''//button[@class=' x-btn-text x-toolbar-more-icon']''').click()
driver.find_element_by_xpath('''//a/span[contains(text(),'Call Agent')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Call Agent')]''').text)

driver.find_element_by_xpath('''//button[@class=' x-btn-text x-toolbar-more-icon']''').click()
driver.find_element_by_xpath('''//a/span[contains(text(),'Call Center Management')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Call Center Management')]''').text)

driver.find_element_by_xpath('''//button[@class=' x-btn-text x-toolbar-more-icon']''').click()
driver.find_element_by_xpath('''//a/span[contains(text(),'Analysis')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Analysis')]''').text)

driver.find_element_by_xpath('''//button[@class=' x-btn-text x-toolbar-more-icon']''').click()
driver.find_element_by_xpath('''//a/span[contains(text(),'Administration')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Administration')]''').text)

driver.find_element_by_xpath('''//button[@class=' x-btn-text x-toolbar-more-icon']''').click()
driver.find_element_by_xpath('''//a/span[contains(text(),'Workflow')]''').click()
time.sleep(2)
print(driver.find_element_by_xpath('''//div/h2/span[contains(text(),'Workflow')]''').text)


driver.close()