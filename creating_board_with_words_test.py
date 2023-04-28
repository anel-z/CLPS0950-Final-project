import numpy 
from numpy import random

list = ['plb', 'knat', 'cop', 'ethel', 'triangle', ]

x = numpy.chararray(10,10)
for n in range (0,4):
 x[n] = list[n]
print(x)
print('clps')


def test_function(number):
  new_array = random.randint(26, size = 5)
  return new_array

new_array.append