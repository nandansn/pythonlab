import re
import os

#tag = input("enter the tag")

pattern = r'^[<][^/][a-z]+([\s]*[\w\W])*(>$|/>$)'

patternObject = re.compile(pattern)

wd = os.getcwd()

filePath = wd + "\\nanda.html"

file = open(filePath)

countTag = 0

line =""



for line in file.readlines():
    
    line = line.lstrip()
    line = line.rstrip()
    print(line)
    matchedObject = re.match(pattern,line)
    if matchedObject != None:
        countTag+= 1

print("Tag Count:",countTag)


file.close()

file = open(filePath)

tagMap ={}

tagCount = 0

for line in file.readlines():
    line = line.lstrip()
    line = line.rstrip()
    matchedObject = re.match(pattern,line)
    
    if matchedObject != None:
        strtag = matchedObject.group().replace("<","").replace(">","")
        strtag = strtag.split()
        strtag = strtag[0]
        if not tagMap.__contains__(strtag):
            tagMap.update({strtag:1})
        else:
            tagCount = tagMap.get(strtag)
            tagCount += 1
            tagMap.update({strtag:tagCount})

file.close()

print("Map:",tagMap)




