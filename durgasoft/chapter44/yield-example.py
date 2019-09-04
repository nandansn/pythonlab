'''

yield is a keyword in Python that is used to return from a function without destroying the states of its local variable and
when the function is called, the execution starts from the last yield statement. Any function that contains a yield keyword is termed as generator. 
Hence, yield is what makes a generator. yield keyword in Python is less known off but has a greater utility which one can think of.

web crawling, web scraping,reading data from large number of files....

'''
def even(num):
    for i in range(num):
        if i %2 == 0:
            yield i


for i in even(10000000000):
    print (i)
