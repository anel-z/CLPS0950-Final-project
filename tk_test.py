import tkinter as tk

class App:
    def __init__(self):
        # Create a list to store text inputs
        self.entered_words = []

        # Create a window
        self.root = tk.Tk()
        self.root.title("Text Input")

        # Create a text input
        self.text_input = tk.Entry(self.root)
        self.text_input.pack()

        # Create a button to add the text to the list
        self.button = tk.Button(self.root, text="Add Text", command=self.add_text)
        self.button.pack()

        # Run the window
        self.root.mainloop()

    def add_text(self):
        # Get the text from the input and add it to the list
        text = self.text_input.get()
        self.entered_words.append(text)
        print(self.entered_words)

# Create an instance of the App class to run the program
app = App()


window.mainloop()

