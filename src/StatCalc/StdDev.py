<<<<<<< HEAD
from Calculator.Root import squareroot
from StatCalc.Variance import variance


def stddev(x):
    try:
        variance_float = variance(x)
        return squareroot(variance_float)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
=======
from Calculator.Root import squareroot
from StatCalc.Variance import variance


def stddev(x):
    try:
        variance_float = variance(x)
        return squareroot(variance_float)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
>>>>>>> origin/master
        print("Invalid Data")