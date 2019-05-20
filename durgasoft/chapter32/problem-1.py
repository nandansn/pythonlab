word='nanda'

vowels=['a','e','i','o','u']

l =[]

l = [c for c in word[:] if (c in vowels and c not in l) ]

print(l)