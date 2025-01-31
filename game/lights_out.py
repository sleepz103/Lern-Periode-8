import tkinter as tkinter
from tkinter import *
from button import GameButton
# create game window
window = tkinter.Tk()
window.title("Lights out")
window.geometry("600x400")

# create 1x2x1 grid
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight= 1)
window.grid_columnconfigure(1, weight=2)
window.grid_columnconfigure(2, weight= 1)


# create game in middle cell
gameBox = Frame(window)
gameBox.grid(row=0,column=1,sticky="nesw")
gridSize = 5
gridDict = {}

for i in range(gridSize):
    gameBox.grid_rowconfigure(i, weight=1)
    gameBox.grid_columnconfigure(i, weight=1)

buttons = []
for row in range(gridSize):
    row_buttons = []
    for col in range(gridSize):
        gameButton = GameButton(row, col, gridDict, gameBox)
        gameButton.grid(row=row, column=col, sticky='nesw')
        row_buttons.append(gameButton)
        gridDict[(row, col)] = gameButton
    buttons.append(row_buttons)
    
window.mainloop()