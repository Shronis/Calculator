from Calculator.calculator import Calculator
from StatCalc.Mean import mean

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def population_mean(self, data):
        self.result = mean(data)
        return self.result