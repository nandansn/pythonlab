import re

nameOne ='Nanda'
nameTwo ='Nanda'

totalNamesLength = nameOne + nameTwo

totalMatchedLength =0

for i in nameOne:
    matchedPatttern = re.findall(i,nameTwo)
    totalMatchedLength = totalMatchedLength + len(matchedPatttern)

print(totalMatchedLength)