import tkinter as tk

# Create a list of letters for the grid
letters = ['A', 'B', 'C', 'D', 'E',
           'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y']

# Create the tkinter window and canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Keep track of the starting and ending cells of the drag selection
start_cell = None
end_cell = None

# Create a function to handle mouse button press events on the canvas
def on_press(event):
    global start_cell, end_cell
    # Get the x and y coordinates of the mouse click
    x, y = event.x, event.y
    # Convert the x and y coordinates to row and column indices
    row = int(y / 60)
    col = int(x / 60)
    # Set the starting cell of the drag selection
    start_cell = (row, col)

# Create a function to handle mouse drag events on the canvas
def on_drag(event):
    global start_cell, end_cell
    # Get the x and y coordinates of the mouse drag
    x, y = event.x, event.y
    # Convert the x and y coordinates to row and column indices
    row = int(y / 60)
    col = int(x / 60)
    # Set the ending cell of the drag selection
    end_cell = (row, col)
    # Redraw the grid to show the current selection
    draw_grid()

# Create a function to draw the grid and highlight the selected cells
def draw_grid():
    canvas.delete('all')
    for i in range(5):
        for j in range(5):
            # Calculate the x and y coordinates of the current cell
            x0 = j * 60
            y0 = i * 60
            x1 = x0 + 60
            y1 = y0 + 60
            
            # Get the index of the current letter in the letters list
            index = (i * 5) + j
            
            # Get the current letter from the letters list
            letter = letters[index]
            
            # Draw the cell background
            fill = 'white'
            if (start_cell is not None and end_cell is not None and
                    start_cell[0] <= i <= end_cell[0] and
                    start_cell[1] <= j <= end_cell[1]):
                fill = 'lightblue'
            canvas.create_rectangle(x0, y0, x1, y1, fill=fill, width=1)
            
            # Draw the letter on the canvas
            canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=letter)

# Bind the mouse click event to the canvas
canvas.bind('<Button-1>', '>B1-Motion<', on_click)