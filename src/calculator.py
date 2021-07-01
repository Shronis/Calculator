from csvReader import CsvReader

def addition(a,b):
    a = int(a)
    b = int(b)
    c = a + b
    return c

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

def square(a):
    return a*a

def squareroot(a):
    return a ** .5

class Calculator:
    result = 0

    def __init__(self):
        x = 2 + 2
        self.result = x;
        pass

    def add(self,a,b):
        self.result = addition(a,b)
        return self.result

    def sub(self,a,b):
        self.result = subtraction(a,b)
        return self.result

    def mul(self,a,b):
        self.result = multiplication(a,b)
        return self.result

    def div(self,a,b):
        self.result = division(a,b)
        return self.result

    def sqr(self,a):
        self.result = square(a)
        return self.result

    def sqrt(self,a):
        self.result = squareroot(a)
        return self.result