import re
import os

filePath = os.getcwd()

pattern = r"(<)(\w+@epam.com)(>)"

fileName = "\\mail.txt"

patternObject = re.compile(pattern)

mailList = ""


file = open(filePath+fileName)

for line in file.readlines():
    
    matchedObjects = re.finditer(patternObject,line)
    
    for matchedObject in matchedObjects:
        mail = matchedObject.groups()[1]
        mailList = mailList + mail + ";"

print(mailList)