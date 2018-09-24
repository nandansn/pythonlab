import re

pattern = re.compile(r'@([\w]+).[\w]+')

inputString = input("Enter input string:")

domainMatched = pattern.search(inputString)

if domainMatched:
    print(domainMatched.group())

    domainStr = domainMatched.group()

    print(domainStr)
    
    print(domainStr[domainStr.index('@')+1:domainStr.index('.')])
    



