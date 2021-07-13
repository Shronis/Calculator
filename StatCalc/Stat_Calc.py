<<<<<<< HEAD
from Calculator.calculator import Calculator
from StatCalc.Mean import mean
from StatCalc.Median import median
from StatCalc.Mode import mode
from StatCalc.Variance import variance
from StatCalc.StdDev import stddev
from StatCalc.RandomSeed import random_seed
from StatCalc.Random_Num import random_num
from StatCalc.Random_Number_List import random_num_list


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def stddev(self, data):
        self.result = stddev(data)
        return self.result

    def random_seed(self, x,y):
        self.result = random_seed(x,y)
        return self.result

    def random_seed(self):
        self.result = random_num()
        return self.result

    def random_seed(self, x,y,n):
        self.result = random_num_list(x,y,n)
=======
from Calculator.calculator import Calculator
from StatCalc.Mean import mean
from StatCalc.Median import median
from StatCalc.Mode import mode
from StatCalc.Variance import variance
from StatCalc.StdDev import stddev
from StatCalc.RandomSeed import random_seed
from StatCalc.Random_Num import random_num
from StatCalc.Random_Number_List import random_num_list


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def variance(self, data):
        self.result = variance(data)
        return self.result

    def stddev(self, data):
        self.result = stddev(data)
        return self.result

    def random_seed(self, x,y):
        self.result = random_seed(x,y)
        return self.result

    def random_seed(self):
        self.result = random_num()
        return self.result

    def random_seed(self, x,y,n):
        self.result = random_num_list(x,y,n)
>>>>>>> origin/master
        return self.result