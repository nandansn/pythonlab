# Python has a built-in function open() to open a file. This function returns a file object,
# also called a handle, as it is used to read or modify the file accordingly.

# 'r'	Open a file for reading. (default)
# 'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# 'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
# 'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# 't'	Open in text mode. (default)
# 'b'	Open in binary mode.
# '+'	Open a file for updating (reading and writing)

fileToRead = open("readme.txt",'r',encoding = 'utf-8')



print(fileToRead.name)

print("File Content:")
len = fileToRead.read().__len__()

# to close a file
fileToRead.close()
print(len)
if  len < 11 :
    fileToWrite = open("readme.txt",'w',encoding = 'utf-8')
    fileToWrite.write("first line success")

fileToRead = open("readme.txt",'r',encoding = 'utf-8')
print(fileToRead.readline())
