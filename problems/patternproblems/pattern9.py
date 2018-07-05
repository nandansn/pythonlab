letters = ''

for i in range(ord('E'),ord('A')-1, -1):
    for k in range(ord('E'),ord('A')-1, -1):
        letters = letters + chr(i)
    print(letters)
    letters=''