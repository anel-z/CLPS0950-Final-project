from only_the_words import word_list_spring
from only_the_words import word_list_school
import random


words_for_board = random.sample(word_list_school, 8)
print('word bank')
#print(len(words_for_board))

big_lists = []

for word in words_for_board:
    letter_list = []
    for letter in word:
        letter_list.append(letter)
    big_lists.append(letter_list)


print(words_for_board)
print(big_lists)