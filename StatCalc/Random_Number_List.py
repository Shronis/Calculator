
import random

def random_num_list(x,y,n):
    num_list = []

    for i in range(0, n):
        hold = random.uniform(x, y)
        num_list.append(hold)

    return num_list
>>>>>>> origin/master
