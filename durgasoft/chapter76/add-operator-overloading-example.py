class Book:
    def __init__(self,pages):
        self.pages = pages


    
    def __add__(self,book1):
        sum = self.pages + book1.pages
        return sum


b = Book(100)
c = Book(200)

print(b + c)