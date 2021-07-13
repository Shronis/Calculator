# <<<<<<< HEAD
from Calculator.Division import division

def mean(x):
    try:
        num_values = len(x)
        total = sum(x)
        return division(total, num_values)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
# =======
from Calculator.Division import division

def mean(x):
    try:
        num_values = len(x)
        total = sum(x)
        return division(total, num_values)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
# >>>>>>> origin/master
        print("Invalid Data")
