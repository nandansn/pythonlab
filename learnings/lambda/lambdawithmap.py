numbers =[10,12,13,14]

f = lambda num: num * 2

def displayNums(nums):
    for num in nums:
        print(num)

t = map(f,numbers)

displayNums(t)

t = map(lambda x: x + 2, numbers)

displayNums(t)



