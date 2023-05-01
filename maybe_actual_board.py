from only_the_words import word_list_spring
from only_the_words import word_list_school
from only_the_words import word_list_music 
from only_the_words import  word_list_sports
from check_fit_function import check_fit
import random


def generate_board(num):
    from initial_random_board import board
    return board(num)

words_for_board = random.sample(word_list_school, 8)
print('word bank')
print(words_for_board)


individual_letters = []

for word in words_for_board:
    letter_list = []
    for letter in word:
        letter_list.append(letter)
    individual_letters.append(letter_list)

print(individual_letters)



used_indices = []
searchboard = generate_board(15)

for n in range (0, len(words_for_board)):
  len_word = len(words_for_board[n])
  size_board = len(searchboard)
  row_index = random.randint(0, size_board-1 )
  column_index = random.randint(0, len(searchboard[0])-1)
  random_index = (row_index, column_index)
  check_fit(row_index, column_index, len_word, size_board)
  direction = random.sample(directions, 1)
  print(direction)













# for n in range (0, len(words_for_board)):
#     len_word = len(words_for_board[n])
#     print(len_word)
#     size_board = len(searchboard)
#     for x in range (0, len_word):
#       row_index = random.randint(0, size_board-1 )
#       column_index = random.randint(0, len(searchboard[0])-1)
#       random_index = (row_index, column_index)
#       if size_board - column_index >= len_word: ###need to add something -- and none of the indices from the random index down to word length are in the list used indices
#         for i in range (column_index, column_index + len_word):
#          if (row_index, i) in used_indices:
#           for p in range (row_index, row_index + len_word):
#             if (p, column_index) in used_indices:
#                break
#             else:
#              for letter in range (0, len_word):
#               searchboard[p] [column_index] = individual_letters[n][letter] 
#               used_indices.append((p,column_index))
#          else:
#           for letter in range (0, len_word):
#             searchboard[row_index] [i] = individual_letters[n][letter]
#             used_indices.append((row_index,i))
#       else:
#          used_indices.append((column_index, row_index))
        
#          ### need to add a pick a new index12cx and not just don't replace it 
# print(used_indices)
# print(searchboard)   












# #generating a random index to test 
# row_index = random.randint(0, len(searchboard) )
# column_index = random.randint(0, len(searchboard[0]))
# random_index = (row_index, column_index)
# print(random_index)




#used_indices = []
#searchboard = generate_board(15)
#for n in range (0, len(words_for_board)):
  #for x in range (0, len(big_lists[n])):
   # searchboard[x,n] = big_lists[n][x]
   # used_indices.append((n,x))
#print(used_indices)
#print(searchboard) 