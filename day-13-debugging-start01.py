#!/usr/bin/env python
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# range(stop) Return an object that produces a sequence of integers
# from start (inclusive) to stop (exclusive)[!!!] by step.
print(f' 1. cell '.center(50, '-'))
logging.debug(f'Start of Program')
def my_function():
  logging.debug(f'Start of my_function')
  for i in range(1, 10):
    logging.debug(f'i is {i}')
    if i == 10:
      logging.debug(f'is {i} == 20?')
      print("You got it")
  logging.debug(f'End of my_function')
my_function()
logging.debug(f'End of Program')


print(f' 2. cell '.center(50, '-'))
# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
# randint() = Return random integer in range [a, b], including[!!!] both end points.
# range(stop) Return an object that produces a sequence of integers
# from start (inclusive) to stop (exclusive)[!!!] by step.
dice_num = 6
print(dice_imgs[dice_num])
