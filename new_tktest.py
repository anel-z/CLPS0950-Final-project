from only_the_words import word_list_spring
from only_the_words import word_list_school

import tkinter as tk

entered_words = []

#stores input in user_input and appends it to entered_words list
#prints both last entered word and list with all entered words

def store_input():
    global user_input
    user_input = entry.get()
    print("Input stored:", user_input)
    entered_words.append(user_input)
    print(entered_words)

# i used spring list but maybe later we could find a way to integrate 
# several lists
if user_input in word_list_spring:
    print('You found the word!')

# Create a window
root = tk.Tk()

# Create an entry box
entry = tk.Entry(root)
entry.pack()

# Create a button to store the input
button = tk.Button(root, text="Check my word!", command=store_input)
button.pack()



# Start the GUI event loop
root.mainloop()
