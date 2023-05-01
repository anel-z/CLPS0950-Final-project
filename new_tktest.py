from only_the_words import word_list_spring
from only_the_words import word_list_school
from maybe_actual_board import words_for_board, searchboard

import tkinter as tk
from tkinter import messagebox

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
        print('You found a word!')
        messagebox.showinfo("Popup Message", "You found a word!")
    else:
        print('Wrong word!!')
        messagebox.showinfo("Popup Message", "Wrong word!!")
# Create a function to update the entered words listbox
def update_words_listbox():
    words_listbox.delete(0, tk.END)
    for word in entered_words:
        words_listbox.insert(tk.END, word)

# Create a listbox to display the entered words
words_listbox = tk.Listbox(root, width=12, height=4)
words_listbox.pack(side=tk.BOTTOM)

# Create a label for the entered words listbox
words_label = tk.Label(root, text="Previous attempts:")
words_label.pack(side=tk.BOTTOM)


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

# Create a button to store the input and update the listbox
button = tk.Button(root, text="Check my word!", command=lambda:[store_input(), update_words_listbox()])
button.pack()



# Start the GUI event loop
root.mainloop()
