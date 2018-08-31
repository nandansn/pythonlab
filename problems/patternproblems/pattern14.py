alphabets=''

for i in range(ord('A'),ord('E')+1):
    for k in range(ord('A'),i+1):
        alphabets = alphabets + chr(k)
    print(alphabets)
    alphabets=''