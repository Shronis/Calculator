
from Calculator.Square import square
from Calculator.Division import division
from StatCalc.Mean import mean


def variance(x):
    try:
        meanx = mean(x)
        num_values = len(x)
        k = 0
        for i in x:
            k = k + square(i-meanx)
        return division(k, num_values)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
        print("Invalid Data")
