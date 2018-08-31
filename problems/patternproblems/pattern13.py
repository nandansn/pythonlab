k =0;
alphabets=''
for i in range(ord('A'),ord('F')):
    for k in range(i,i+1):
        alphabets = alphabets + chr(i) * (k+1 - k)
      
    print(alphabets)