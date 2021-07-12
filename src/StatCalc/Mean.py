from Calculator.Division import division

def mean(x):
    try:
        num_values = len(x)
        total = sum(x)
        return division(total, num_values)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")