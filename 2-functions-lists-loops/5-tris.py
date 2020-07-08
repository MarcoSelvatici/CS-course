import tkinter as tk

# TODO: implement this function.
# Input: the grid - list of lists containing either "X", "O", or "-".
# Output: "X" if player "X" won.
#         "O" if player "O" won.
#         "-" if nobody won.
def check_victory(grid):
    return "-"





root = tk.Tk() # Create a window.
turn = "X"     # Set the initial turn.
grid = [       # Set the initial grid.
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

def advanceTurn():
    global turn
    # The next line is equivalent to:
    # if turn == "X":
    #     turn = "O"
    # else:
    #     turn = "X"
    turn = "O" if turn == "X" else "X"

# Create a button with the given text in the specific row and column.
def makeButton(r, c, text):
    button = tk.Button(root, text=text, borderwidth=1, width=5, height=3)
    button.grid(row=r, column=c)

# Handle clicks.
def handleClick(event):
    # Find out the column and row of the click.
    x = event.x_root - root.winfo_rootx() 
    y = event.y_root - root.winfo_rooty() 
    c, r = root.grid_location(x, y)
    # If the cell is not yet used, the assign it to the player and advance the turn.
    if grid[r][c] == "-":
        grid[r][c] = turn
        makeButton(r, c, turn)
        advanceTurn()
    # Check winner.
    winner = check_victory(grid)
    if winner != "-":
        # Show the winner banner.
        text = f"Winner is {winner}"
        label = tk.Label(root, text=text, bg="yellow", font=("Courier", 17))
        label.place(x=25, y=50)

# Initialise the interface with only "-".
def initialiseGrid():
    for r in range(3):
        for c in range(3):
            makeButton(r, c, "-")

initialiseGrid()

root.bind("<Button-1>", handleClick) # Make the interface clickable.
root.mainloop()                      # Start the interface.
