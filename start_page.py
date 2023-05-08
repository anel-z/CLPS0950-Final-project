import tkinter as tk
import subprocess

root = tk.Tk()

#welcome text
title_label = tk.Label(root, text="Welcome to Wordsearch!", font = ("Helvetica", 30))
next_label = tk.Label(root, text ="To start, pick a wordsearch topic:", font=("Helvetica", 22))
title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=20)
next_label.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

spring_button = tk.Button(root, text="Spring", command=lambda: generate_wordsearch("spring_game.py"))
school_button = tk.Button(root, text="School", command=lambda: generate_wordsearch("school_game.py"))
music_button = tk.Button(root, text="Music", command=lambda: generate_wordsearch("music_game.py"))
sports_button = tk.Button(root, text="Sports", command=lambda: generate_wordsearch("sports_game.py"))

def generate_wordsearch (filename):
    subprocess.run(["python", filename])

spring_button.grid(row=4, column=0, padx=10, pady=10)
school_button.grid(row=4, column=1, padx=10, pady=10)
music_button.grid(row=5, column=0, padx=10, pady=10)
sports_button.grid(row=5, column=1, padx=10, pady=10)

root.mainloop()