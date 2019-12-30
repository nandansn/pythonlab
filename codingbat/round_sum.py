def round_sum(a,b,c):
    lastDigit = extract_last_digit(a)
    a = round_num(lastDigit, a)

    lastDigit = extract_last_digit(b)
    b = round_num(lastDigit, b)

    lastDigit = extract_last_digit(c)
    c = round_num(lastDigit, c)

    print(a+b+c)




def extract_last_digit(num):
    if num > 9 :
        lastDigit = num % 10
        return lastDigit
    else:
        return num

def round_num(lastDigit, num):
    if lastDigit > 4:
        bal = 10 - lastDigit
        return num + bal
    else:
        return num - lastDigit


a = eval(input('a:'))
b = eval(input('b:'))
c = eval(input('c:'))

round_sum(a,b,c)