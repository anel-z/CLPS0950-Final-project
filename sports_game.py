from actual_board_sports import words_for_board_sports, searchboard, letter_positions

import tkinter as tk
from tkinter import messagebox

entered_words = []
correct_words = []

# Create a window
root = tk.Tk()
global user_input
user_input = ''

#stores input in user_input and appends it to entered_words list
#prints both last entered word and list with all entered words
#checks if user_input is a correct word, tells you how many you've found in total if so
#messages tell you if it's correct, wrong, or already entered
#final message says you've found all words.
def store_input():
    global user_input
    user_input = entry.get()
    print("Input stored:", user_input)
    entered_words.append(user_input)
    print(entered_words)
    global correct_words
    if user_input in correct_words:
        messagebox.showinfo("Popup Message", "You've already entered this word.")
    elif (user_input in words_for_board_sports) and len(correct_words)<7:
        print('You found a word!')
        messagebox.showinfo("Popup Message", "You found a word!")
        correct_words.append(user_input)
        update_letter_colors()

    elif (user_input in words_for_board_sports) and len(correct_words)==7:
        correct_words.append(user_input)
        messagebox.showinfo("Popup Message", "You found all the words! Yay!!" )
        update_letter_colors()
    else:
        print('Wrong word!!')
        messagebox.showinfo("Popup Message", "Wrong word!!")
        return
    
   
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

text_box = tk.Text(root, height=1, width=30)
def score_textbox():
    global text_box
    correct_score = len(correct_words)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, f"You've found {correct_score} / 8 words!")
def update_text_box():
    score_textbox()
    root.after(1000, update_text_box) # Update the text box every second


score_textbox()

text_box.pack(side=tk.BOTTOM)

update_text_box()

# displays grid from searchboard to window 
#grid = tk.Listbox(root, width=45, height=15, justify='center')
#grid.pack()

    
# Create a frame to hold the grid of letters
grid_frame = tk.Frame(root)
grid_frame.pack()

letter_labelss = []
# Use a nested loop to create a grid of labels to display the letters
for i in range(len(searchboard)):
    for j in range(len(searchboard[i])):
        # Create a label for the letter and add it to the grid frame
        letter_label = tk.Label(grid_frame, text=searchboard[i][j], width=3, height=1, font=("Helvetica", 15))
        letter_label.grid(row=i, column=j)
        letter_labelss.append(letter_label)



def update_letter_colors():
    global user_input
    print('updating colors')
    # Iterate through all the labels and change the color if the word is found
    for i, letter_label in enumerate(letter_labelss):
        if i in letter_positions.get(user_input,[]):
            letter_label.config(fg='red')
            print(f'updating letter {searchboard[i//15][i%15]}')
            letter_label.update()
        #else:
            #letter_label.config(fg='black')
            #letter_label.update()
    grid_frame.update()
    #root.after(100, update_letter_colors) # Update the color every 100 milliseconds

# Call the update_letter_colors function to start updating the colors
update_letter_colors()


# Create an entry box
entry = tk.Entry(root)
entry.pack()

# Create a button to store the input and update the listbox
button = tk.Button(root, text="Check my word!", command=lambda:[store_input(), update_words_listbox()])
button.pack()


# Start the GUI event loop
root.mainloop()

