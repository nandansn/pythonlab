'''
To store data for future in file.

Types of files,
1. Text
2. Binary


Opeaning a file,
1. open file, specify the purpose, like read, write, append
2. we have python in built function, open(),
3. mode: r - is read mode
4. mode: w - is write mode, override existing file, specified file not available will create new file.
5. mode: a - is append mode, it will not override. it will append the data
6. mode: r+ - is read and write mode. file pointer will point to begining of the line. first read and write.
7. Mode: w+ - is write and read mode. file pointer will point to begining line.
8. Mode a+ - append the data and read the data, will not override the existing data.
9. Mode x - to open a file in exclusive creation mode for write operation. if the file exists error will be thrown, will create new file.

For binary files, 
above mode will be suffixed with b, like rb, wb, ab, r+b, w+b, a+b xb.

Closing file:
close()


Reading from the file :
read() - to read all the data from the file.
read(n) - to read n chars from the file.
readLine() - read line by line.
readLines() - to read all lines into a list.

with Statement:
will take care of closing of the file, after all file operations

with open('file.txt','w') as f:

tell():
    gives the file pointer position in the file.

offset():
    number of positions,
    how many numbers of positions you want to move,
    from where.

        0 -> from begining of the file
        1 -> from current position of the file
        2 -> from end of the file


How to check if the file exists or not:
       using OS module,
        we have path sub-module
'''