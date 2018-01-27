import os

print(os.getcwd())

file = open("c:\\Users\\nandakumar_rangasamy\\git-repo\\pythonlab\\learnings\\StringFormatting\\"+"nanda.txt")

names=[]

for line in file.readlines():
    names.append(line)

for name in names:
    namesplit = name.split(";")
    print(namesplit)
    strp = "~".join(namesplit)
    print(strp.split("~",1))






     