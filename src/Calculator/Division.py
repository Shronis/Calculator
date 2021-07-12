<<<<<<< HEAD
def division(a, b):
    try:
        return round((float(a) / float(b)), 9)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
=======
def division(a, b):
    try:
        return round((float(a) / float(b)), 9)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
>>>>>>> origin/master
        print("Invalid Data")