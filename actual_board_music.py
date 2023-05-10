from only_the_words import word_list_music
from check_fit_function import check_fit
import numpy as np
import random

##see actual_board_spring for commented code

def generate_board(num):
    from initial_random_board import board
    return board(num)

words_for_board_music = random.sample(word_list_music, 8)
print('word bank')
print(words_for_board_music)


individual_letters = []

for word in words_for_board_music:
    letter_list = []
    for letter in word:
        letter_list.append(letter)
    individual_letters.append(letter_list)

print(individual_letters)

used_indices = []
searchboard = generate_board(15)

n=0
letter_positions = {w : [] for w in words_for_board_music}
while n<len(words_for_board_music):
  possible_directions = []
  print(words_for_board_music[n])
  while possible_directions == []:
    len_word = len(words_for_board_music[n])
    size_board = len(searchboard)
    row_index = random.randint(0, size_board-1)
    column_index = random.randint(0, size_board-1)
    random_index = (row_index, column_index)
    possible_directions = check_fit(row_index, column_index, len_word, size_board, used_indices)
    print(possible_directions)


  direction = random.sample(possible_directions, 1)
  print(direction)

  if direction[0] == 'horizontal left':
    print("here 1")
    for x in range (0, (len_word)):
      print(individual_letters[n][x])
      searchboard[row_index] [column_index - x] = individual_letters[n][x]
      letter_positions[words_for_board_music[n]].append(row_index * 15 + (column_index - x))
      used_indices.append((row_index, column_index - x))

  elif direction[0] == 'horizontal right':
    print('here 2')
    for x in range (0, (len_word)):
      print(individual_letters[n][x])
      searchboard[row_index] [column_index + x] = individual_letters[n][x]
      letter_positions[words_for_board_music[n]].append(row_index * 15 + (column_index + x))
      used_indices.append((row_index, column_index + x))
    
  elif direction[0] == 'vertical up':
    print("here 3")
    for x in range (0, (len_word)):
      print(individual_letters[n][x])
      searchboard[row_index-x][column_index] = individual_letters[n][x]
      letter_positions[words_for_board_music[n]].append((row_index-x) * 15 + column_index)
      used_indices.append((row_index-x, column_index))
    
  elif direction[0] == 'vertical down':
    print("here 4")
    for x in range (0, len_word):
      print(individual_letters[n][x])
      searchboard[row_index+x][column_index] = individual_letters[n][x]
      letter_positions[words_for_board_music[n]].append((row_index+x) * 15 + column_index)
      used_indices.append((row_index+x, column_index))
 
  elif direction[0] == 'diagonal top to bottom':
    print("here 5")
    for x in range (0, len_word):
      print(individual_letters[n][x])
      searchboard[row_index+x] [column_index-x] = individual_letters[n][x]
      letter_positions[words_for_board_music[n]].append((row_index+x) * 15 + (column_index-x))
      used_indices.append((row_index+x, column_index-x))

  elif direction[0] == 'diagonal bottom to top':
    print("here 6")
    for x in range (0, len_word):
      print(individual_letters[n][x])
      searchboard[row_index-x] [column_index+x] = individual_letters[n][x]
      letter_positions[words_for_board_music[n]].append((row_index-x) * 15 + (column_index+x))
      used_indices.append((row_index-x, column_index+x))
  print('at the end of outer while loop',used_indices)

  #words_for_board.pop(0)
  n += 1 
  print(words_for_board_music)

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

for row in searchboard:
    for letter in row:
        print(letter, end=' ')
    print()

