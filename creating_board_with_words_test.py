import numpy 
from numpy import random




list = ['plb', 'knat', 'cop', 'ethel', 'triangle', ]
word_list_spring = ['baseball', 'allergies', 'easter', 'passover', 'cleaning', 'breeze', 'butterfly', 'fertilizer', 'green', 'garden', 'seeds', 'season', 'sapling', 'waterfall', 'grass', 'floral', 'orchid', 'nature', 'rainbow', 'rebirth', 'sundress', 'tulip', 'yard', 'taxes', 'cheerful' 'bloom','blossom', 'flower', 'revival', 'warm', 'tree', 'pollen', 'glory', 'daffodil', 'lavendar', 'splendor', 'balmy', 'equinox', 'germinate', 'hatch', 'prune', 'sapling', 'sprout', 'vernal', 'energized', 'daylight', 'sunshine', 'brisk', 'april' ,'may', 'finals']
shorten = word_list_spring[:4]

big_lists = []

for word in shorten:
    letter_list = []
    for letter in word:
        letter_list.append(letter)
    big_lists.append(letter_list)

print(big_lists)
for n in range (0, len(shorten)):
  for x in range (0, len(big_lists[n])):
    print(big_lists[n][x])

x = numpy.chararray(10,10)
for n in range (0,4):
 x[n] = big_lists[n]
print(x)
print('clps')


