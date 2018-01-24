import os

path = os.getcwd()
file = open(path+"\\learnings\\codingbat\\files\\"+"nanda.txt","a") # append mode

print(file)

if file.writable:
    print("file is writable")
    length = file.write("python is simple. \n i like it")
    print(length)

#file.close()

if file.readable():
    for line in file.readlines():
        print(line)
else:
    file = open(path+"\\learnings\\codingbat\\files\\"+"nanda.txt","r")
    for line in file.readlines():
        print(line)

file.close()

file = open(path+"\\learnings\\codingbat\\files\\"+"nanda.txt","w") # write mode - overwrite

names = ['java','python','javascript','groovy']

for name in names:
    file.write(name+"\n")

file.close()

file = open(path+"\\learnings\\codingbat\\files\\"+"nanda.txt","r") # read mode

for line in file.readlines():
    print(line)

file.close()
    
file = open(path+"\\learnings\\codingbat\\files\\"+"sample.txt","r",encoding="utf8") # read mode

print("number of lines:",len(file.readlines()))