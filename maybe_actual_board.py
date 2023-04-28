from only_the_words import word_list_spring
from only_the_words import word_list_school
import random


def generate_board(num):
    from initial_random_board import board
    return board(num)



words_for_board = random.sample(word_list_school, 8)
print('word bank')
print(words_for_board)
#print(len(words_for_board))

big_lists = []

for word in words_for_board:
    letter_list = []
    for letter in word:
        letter_list.append(letter)
    big_lists.append(letter_list)


print(words_for_board)
print(letter_list)
print(big_lists)



#for n in range (0, len(words_for_board)):
#  for x in range (0, len(big_lists[n])):
  #  print(big_lists[n][x])


used_indices = []
searchboard = generate_board(15)
for n in range (0, len(words_for_board)):
    for x in range (0, len(big_lists[n])):
      row_index = random.randint(0, len(searchboard)-1 )
      column_index = random.randint(0, len(searchboard[0])-1)
      random_index = (row_index, column_index)
      if len(searchboard) - column_index >= len(words_for_board[n]):
        for i in range (0, len(words_for_board[n])):
         searchboard[row_index, column_index + i] = big_lists[n][i]
      else:
         searchboard[column_index, row_index] = 1
         used_indices.append((n,x))
print(used_indices)
print('inserted' 'horizontally')
    
print(searchboard)   


#generating a random index to test 
row_index = random.randint(0, len(searchboard) )
column_index = random.randint(0, len(searchboard[0]))
random_index = (row_index, column_index)
print(random_index)




#used_indices = []
#searchboard = generate_board(15)
#for n in range (0, len(words_for_board)):
  #for x in range (0, len(big_lists[n])):
   # searchboard[x,n] = big_lists[n][x]
   # used_indices.append((n,x))
#print(used_indices)
    
#print(searchboard)   