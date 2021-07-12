import random

def random_seed(x,y):
  try:
    return random.uniform(x,y)
  except ValueError:
      print("Invalid Data")