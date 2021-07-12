def multiplication(a, b):
    try:
        return float(a) * float(b)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
        print("Invalid Data")