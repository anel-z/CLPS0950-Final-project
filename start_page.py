import tkinter as tk
root = tk.Tk()

#welcome text
title_label = tk.Label(root, text="Welcome to Wordsearch!", font = ("Helvetica", 30))
next_label = tk.Label(root, text ="To start, pick a wordsearch topic:", font=("Helvetica", 22))
title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
next_label.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

#topic option buttons
def start_spring_game():
    import spring_game
    spring_game.play_game()
spring_button = tk.Button (root, text="spring", command=start_spring_game)
spring_button.pack()

root.mainloop()