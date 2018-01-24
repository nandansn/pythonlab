import os

path = os.getcwd()
print (path)

file = open(path+"\\learnings\\codingbat\\files\\nanda.txt")

file.name

for line in file.readlines():
    print (line)

currentFilePosition = file.tell()
print(currentFilePosition)

file.close()
if file.closed:
    print("File closed successfully")