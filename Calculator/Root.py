<<<<<<< HEAD
def squareroot(a):
    try:
        return round((float(a)**.5), 9)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
=======
def squareroot(a):
    try:
        return round((float(a)**.5), 9)
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
>>>>>>> origin/master
        print("Invalid Data")