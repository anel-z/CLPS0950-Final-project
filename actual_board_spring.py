from only_the_words import word_list_spring
from check_fit_function import check_fit
import numpy as np
import random

#importing the random board
def generate_board(num):
    from initial_random_board import board
    return board(num)

#generating the words that willl be inserted into the board
words_for_board_spring = random.sample(word_list_spring, 8)
print('word bank')
print(words_for_board_spring)


#separating each word into its own list with each letter as an element
individual_letters = []

for word in words_for_board_spring:
    letter_list = []
    for letter in word:
        letter_list.append(letter)
    individual_letters.append(letter_list)

print(individual_letters)


#filling the board with the words using a series of loops. indices get appended to used_indices once the word is entered into the board
used_indices = []
searchboard = generate_board(15)

n=0
letter_positions = {w : [] for w in words_for_board_spring}
while n<len(words_for_board_spring):
  possible_directions = []
  print(words_for_board_spring[n])
  while possible_directions == []:
    len_word = len(words_for_board_spring[n])
    size_board = len(searchboard)
    row_index = random.randint(0, size_board-1) 
    column_index = random.randint(0, size_board-1)
    random_index = (row_index, column_index) #random index from which to check the possible directions 
    possible_directions = check_fit(row_index, column_index, len_word, size_board, used_indices) #calling the check_fit function to generate list of possible directions for the word
    print(possible_directions)


  direction = random.sample(possible_directions, 1) #randomly pick one of the possible directions to actually implement 
  print(direction)

  #adding the words into the board based on the chosen direction

  if direction[0] == 'horizontal left': 
    for x in range (0, (len_word)):
      print(individual_letters[n][x])
      searchboard[row_index] [column_index - x] = individual_letters[n][x]
      letter_positions[words_for_board_spring[n]].append(row_index * 15 + (column_index - x))
      used_indices.append((row_index, column_index - x))

  elif direction[0] == 'horizontal right':
    for x in range (0, (len_word)):
      print(individual_letters[n][x])
      searchboard[row_index] [column_index + x] = individual_letters[n][x]
      letter_positions[words_for_board_spring[n]].append(row_index * 15 + (column_index + x))
      used_indices.append((row_index, column_index + x))
    
  elif direction[0] == 'vertical up':
    for x in range (0, (len_word)):
      print(individual_letters[n][x])
      searchboard[row_index-x][column_index] = individual_letters[n][x]
      letter_positions[words_for_board_spring[n]].append((row_index-x) * 15 + column_index)
      used_indices.append((row_index-x, column_index))
    
  elif direction[0] == 'vertical down':
    for x in range (0, len_word):
      print(individual_letters[n][x])
      searchboard[row_index+x][column_index] = individual_letters[n][x]
      letter_positions[words_for_board_spring[n]].append((row_index+x) * 15 + column_index)
      used_indices.append((row_index+x, column_index))
 
  elif direction[0] == 'diagonal top to bottom':
    for x in range (0, len_word):
      print(individual_letters[n][x])
      searchboard[row_index+x] [column_index-x] = individual_letters[n][x]
      letter_positions[words_for_board_spring[n]].append((row_index+x) * 15 + (column_index-x))
      used_indices.append((row_index+x, column_index-x))

  elif direction[0] == 'diagonal bottom to top':
    for x in range (0, len_word):
      print(individual_letters[n][x])
      searchboard[row_index-x] [column_index+x] = individual_letters[n][x]
      letter_positions[words_for_board_spring[n]].append((row_index-x) * 15 + (column_index+x))
      used_indices.append((row_index-x, column_index+x))

  #words_for_board.pop(0)
  n += 1 
  print(words_for_board_spring)

#more troubleshooting 
print(searchboard) 
print(used_indices) 
counter ={}
for d in used_indices:
  if d not in counter:
    counter[d]=0
  counter[d]+=1
if any(np.array(list(counter.values()))>1):
  print('ERROR')
  print(counter)


#getting rid of the '' surrounding each of the letters 
for row in searchboard:
    for letter in row:
        print(letter, end=' ')
    print()

