import re
import os

pattern = r"(\w+)\(((\w+).java):(\d+)"

filePath = os.getcwd()

fileName = "\\mylog.log"

file = open(filePath+fileName)

patternObject = re.compile(pattern)


for line in file.readlines():
    matchedObject =re.search(patternObject,line)
    if matchedObject != None:
        print(matchedObject.groups())
