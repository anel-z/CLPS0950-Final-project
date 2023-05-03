
import numpy as np
from numpy import random
from number2alphabet import NumtoAlph

def board(int):
  array = np.chararray((int,int))
  for n in range (0,int):
    for x in range (0,int):
     array[x,n] = NumtoAlph(random.randint(26))
  return array.decode()
  
 
print(board(15))



