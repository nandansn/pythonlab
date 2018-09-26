characterFrom = input("Enter character from:")
charLen = int(input("Enter number of char:"))

appendChars =''

startAsciiCode = ord(characterFrom)
endAsciiCode = startAsciiCode + charLen
count = 0
for i in range(startAsciiCode,endAsciiCode+1,1):
    appendChars=''
    for j in range(startAsciiCode,endAsciiCode - count,1):
        appendChars = appendChars + chr(j)
    print(appendChars)
    count +=1
