from csvReader import CsvReader
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Square import square
from Calculator.Root import squareroot

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

















class CsvStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass

    def mean(self):
        mean(self.data)