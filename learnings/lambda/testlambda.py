from functools import reduce

f = lambda x: x * 2

print(f(10))

#lambda with map and list

names =['nanda','kumar']

m = map(f,names)

print(list(m))

#lamda with filter

salary = [1000,2000,500,6000,900,200,350]

f = filter(lambda s: s > 1000, salary)

print(list(f))

#lambda with reduce

moreSalary = reduce(lambda x,y: x if (x > y) else y,salary)

print(moreSalary)

totalSalary = reduce(lambda x,y: x + y, salary)

print(totalSalary)