
import numpy as np
from numpy import random
from number2alphabet import NumtoAlph

array = np.chararray((15,15))
for n in range (0,15):
    for x in range (0,15):
     array[x,n] = NumtoAlph(random.randint(26))

  #  array[:,n] = NumtoAlph(random.randint(26))
print(array)


