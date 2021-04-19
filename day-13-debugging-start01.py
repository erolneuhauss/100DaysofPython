#!/usr/bin/env python
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug(f'Start of Program')
def my_function():
  logging.debug(f'Start of my_function')
  for i in range(1, 20):
    logging.debug(f'i is {i}')
    if i == 20:
      logging.debug(f'is {i} == 20?')
      print("You got it")
  logging.debug(f'End of my_function')
my_function()
logging.debug(f'End of Program')
