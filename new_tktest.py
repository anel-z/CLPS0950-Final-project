from only_the_words import word_list_spring
from only_the_words import word_list_school
from maybe_actual_board import words_for_board, searchboard

import tkinter as tk

entered_words = []

# Create a window
root = tk.Tk()

#stores input in user_input and appends it to entered_words list
#prints both last entered word and list with all entered words

def store_input():
    global user_input
    user_input = entry.get()
    print("Input stored:", user_input)
    entered_words.append(user_input)
    print(entered_words)
    if user_input in words_for_board:
        print('You found the word!')
    else:
        print('Wrong word!!')

# displays grid from searchboard to window 
# width and height make window bigger, shows whole grid now
# but the b's are still there!! :(((
grid = tk.Listbox(root, width=45, height=15)
grid.pack()
for item in searchboard:
     grid.insert(tk.END, item)


# Create an entry box
entry = tk.Entry(root)
entry.pack()

# Create a button to store the input
button = tk.Button(root, text="Check my word!", command=store_input)
button.pack()



# Start the GUI event loop
root.mainloop()
