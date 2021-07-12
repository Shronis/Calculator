from Calculator.calculator import Calculator
from StatCalc.Mean import mean
from StatCalc.Median import median

class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def population_mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result