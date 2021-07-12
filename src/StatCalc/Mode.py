<<<<<<< HEAD
from collections import Counter


def mode(x):
    try:
        num_values = len(x)
        count = Counter(x)
        get_mode = dict(count)
        result = [k for k, v in get_mode.items() if v == max(list(count.values()))]
        if len(result) == num_values:
            get_mode = "No mode found"
        else:
            get_mode = result[0]
        return get_mode
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
=======
from collections import Counter


def mode(x):
    try:
        num_values = len(x)
        count = Counter(x)
        get_mode = dict(count)
        result = [k for k, v in get_mode.items() if v == max(list(count.values()))]
        if len(result) == num_values:
            get_mode = "No mode found"
        else:
            get_mode = result[0]
        return get_mode
    except ZeroDivisionError:
        print("Can't Divide by 0")
    except ValueError:
>>>>>>> origin/master
        print("Invalid Data")