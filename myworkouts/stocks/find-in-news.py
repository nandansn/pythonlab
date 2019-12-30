from urllib.request import urlopen
from selenium import webdriver
import time

stockName = input('Enter stock to find:')
pagesFrom = int(input('Enter page from:'))
pagesTo = int(input('Enter page to:'))
openPage = input('Y/N:')

pagesList = {}

for i in range(pagesFrom,pagesTo+1,1):
    url = 'https://www.moneycontrol.com/news/business/stocks/'
    foundInPage = False
    if i > 1:
        url = 'https://www.moneycontrol.com/news/business/stocks/page-'+str(i)+'/'

    #print(url)

    with urlopen(url) as response:
        for line in response:
            line = line.decode('utf-8')
            if stockName in line:
                foundInPage = True
        if foundInPage:
            pagesList[i] = url

if openPage == 'Y':
    for link in pagesList:
        print(pagesList[link])    
        chromeDriver = webdriver.Chrome()
        chromeDriver.get(pagesList[link])
        time.sleep(2)
        chromeDriver.close()



