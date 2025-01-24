import tkinter as tkinter
from tkinter import *
from button import GameButton

window = tkinter.Tk()
window.title("Lights out")
window.geometry("600x400")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight= 1)
window.grid_columnconfigure(1, weight=2)
window.grid_columnconfigure(2, weight= 1)

gameBox = Frame(window)
gameBox.grid(row=0,column=1,sticky="nesw")


for i in range(0,5):
    gameBox.grid_rowconfigure(i, weight=1)
    gameBox.grid_columnconfigure(i, weight=1)

buttons = []
for row in range(0,5):
    row_buttons = []
    for col in range(0,5):
        gameButton = GameButton(row, col, gameBox)
        gameButton.grid(row=row, column=col, sticky='nesw')
        row_buttons.append(gameButton)
    buttons.append(row_buttons)

window.mainloop()