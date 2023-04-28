word_list_spring = ['baseball', 'allergies', 'easter', 'passover', 'cleaning', 'breeze', 'butterfly', 'fertilizer', 'green', 'garden', 'seeds', 'season', 'sapling', 'waterfall', 'grass', 'floral', 'orchid', 'nature', 'rainbow', 'rebirth', 'sundress', 'tulip', 'yard', 'taxes', 'cheerful' 'bloom','blossom', 'flower', 'revival', 'warm', 'tree', 'pollen', 'glory', 'daffodil', 'lavendar', 'splendor', 'balmy', 'equinox', 'germinate', 'hatch', 'prune', 'sapling', 'sprout', 'vernal', 'energized', 'daylight', 'sunshine', 'brisk', 'april' ,'may', 'finals']
print(len(word_list_spring))

word_list_school = ['classroom', 'public', 'private', 'homeschool', 'break', 'bus', 'office', 'bachelors', 'masters', 'phd', 'teacher', 'student', 'college', 'education', 'library', 'kindergarten', 'science', 'learning', 'classmate', 'lab', 'workshop', 'conference', 'work', 'curriculum', 'campus', 'reading', 'discussion', 'graduation', 'commencement', 'convocation', 'teach', 'professor', 'cafeteria', 'concentration', 'certificate', 'research','grade', 'exam', 'midterm', 'finals', 'dropout', 'extracurricular', 'tutorial', 'math', 'literature', 'brown', 'freshman', 'sophomore', 'junior', 'senior']
print(len(word_list_school))

import numpy as np
import random 

#words_for_board = []
#for x in range (random.randint(50), random.randint(50)):
  #words_for_board.append(word_list_school(x))

words_for_board = random.sample(word_list_school, 8)
print(words_for_board)
print(len(words_for_board))


#shorten = word_list_spring[:4]

big_lists = []

for word in words_for_board:
    letter_list = []
    for letter in word:
        letter_list.append(letter)
    big_lists.append(letter_list)

print(big_lists)

for n in range (0, len(words_for_board)):
  for x in range (0, len(big_lists[n])):
    print(big_lists[n][x])
##going forward-- use if statements to figure out which word list to use ? or maybe not even necessary
# figure out with a test version how to replace the values in the array with the letters
## figure out how to randomize the indices of the replacement so don't get same board every time

## cannot figure out how to just import directly
#import numpy as np
#from numpy import random
#from number2alphabet import NumtoAlph
from initial_random_board import board 


#def board(int):
 # array = np.chararray((int,int))
  #for n in range (0,int):
   # for x in range (0,int):
    # array[x,n] = NumtoAlph(random.randint(26))
 # return array

  #  array[:,n] = NumtoAlph(random.randint(26))
  #print(array)


searchboard = board(15)
print('                       ')
for n in range (0, len(words_for_board)):
  for x in range (0, len(big_lists[n])):
    searchboard[x,n] = big_lists[n][x]
print(searchboard)    


##omg omg omg omg it worked!!!!!!

##create a dictionary of used indices-- if it picks one of those, has to pick again
# +1, -1 will give you diagonal 
#develop rules 