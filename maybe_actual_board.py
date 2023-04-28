
import numpy as np
from numpy import random
from number2alphabet import NumtoAlph
import random_word
from random_word import RandomWords
r = RandomWords()


def randomwordfunction(n):
 random_words = [ ]
 for x in range (0,n):
  random_words.append(str(r.get_random_word()))
  

 print(random_words)



def board(int):
  array = np.chararray((int,int))
  for n in range (0,int):
    for x in range (0,int):
     array[x,n] = NumtoAlph(random.randint(26))

     return array

  #  array[:,n] = NumtoAlph(random.randint(26))
  print(array)


my_board = board(15)
my_words = randomwordfunction(5)
#print(my_words[1])

#for n in range (0,5):
 # my_board[random.rand.int(25), random.rand.int(25)] = my_words(n)
#print(my_board)







