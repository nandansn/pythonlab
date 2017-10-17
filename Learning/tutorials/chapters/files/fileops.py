file = open('books',encoding='utf-8')

print(file.readline())

print(file.readlines(3))

file.seek(0)

for line in file:
    print(line)

