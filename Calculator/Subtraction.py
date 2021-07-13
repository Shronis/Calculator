
def subtraction(a, b):
    try:
        return float(b) - float(a)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
        print("Invalid Data")
