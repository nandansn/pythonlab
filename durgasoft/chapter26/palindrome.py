name=input('value:')

if name == ''.join(reversed(name)):
    print('palindrome')
else:
    print('not palindrome')