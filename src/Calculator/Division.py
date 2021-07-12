def division(a, b):
    try:
        return round((float(a) / float(b)), 9)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print ("Error: Check your data inputs")