from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")

try:
    assert "Python" in driver.title
except AssertionError:
    print('Title assertion failed.')

searchElement = driver.find_element_by_name('q')
searchElement.clear()
searchElement.send_keys('Nanda')
searchElement.send_keys(Keys.RETURN)

driver.find_element_by_xpath('//*[@id="form1"]/p/button')



try:
    assert "Nandaset  results found." in driver.page_source
except AssertionError:
    print('Search text assertion failed.')


driver.close()
