<<<<<<< HEAD
def subtraction(a, b):
    try:
        return float(a) - float(b)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
=======
def subtraction(a, b):
    try:
        return float(a) - float(b)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
>>>>>>> origin/master
        print("Invalid Data")