def addition(a, b):

    try:
        return float(a) + float(b)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")