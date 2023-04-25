##import english_words
#from english_words import words

##word_list = list(words)

#print(word_list[:10])


#print(english_words.get_list_of_words()[:10])
#from english_words import get_english_words_set 
#web2lowerset = get_english_words_set (['web2'], lower=True)
#print(english_words.get_english_words_set()[:10])
import random_word
from random_word import RandomWords
r = RandomWords()

# Return a single random word

def randomwordfunction(n):
 random_words = []
 for x in range (0,n):
  random_words.append(r.get_random_word())

 print(random_words)

randomwordfunction(5)

