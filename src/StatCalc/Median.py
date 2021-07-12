from Calculator.Division import division
from Calculator.Subtraction import subtraction
from Calculator.Addition import addition

def median(x):
    try:
        num_values = len(x)
        num_list = [x[i] for i in range(num_values)]
        num_list.sort()
        if num_values % 2 == 0:
            median1 = num_list[int(num_values // 2)]
            median2 = num_list[int(subtraction((num_values // 2), 1))]
            result = division(addition(median1, median2), 2)
        else:
            result = num_list[int(division(num_values, 2))]
        return result
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
        print("Invalid Data")