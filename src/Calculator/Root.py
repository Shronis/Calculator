def squareroot(a):
    try:
        return round((float(a)**.5), 9)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")