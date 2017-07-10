i = 10;

#While, if and break
while i < 20:
    i+=1
    print("nanda")
    if i == 20 :
        print("limit reached")
        break;
    else:
        print("limit not reached")

#While, if and continue
while i < 30:
    i+=2;
    print(i)
    if i == 30:
        i = 29
        continue

#While, else

while i < 40:
    i+=2
    print(i)
else:
    print(i+"limit reached")

