import tkinter as tkinter
from tkinter import *
from button import GameButton
from Game import Game
# create game window
window = tkinter.Tk()
window.title("Lights out")
window.geometry("600x400")

# create 1x2x1 grid
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight= 1)
window.grid_columnconfigure(1, weight=2)
window.grid_columnconfigure(2, weight= 1)

# game size buttons
controlPanel = tkinter.Frame(window)
controlPanel.grid(row=0, column=0,sticky="nesw")

def set_grid_size(size):
    global game
    game.grid_size = size
    game.generate_grid()


tkinter.Button(controlPanel, text="3x3", command=lambda: set_grid_size(3)).pack(fill="x")  # Button for 3x3 grid
tkinter.Button(controlPanel, text="5x5", command=lambda: set_grid_size(5)).pack(fill="x")  # Button for 5x5 grid

game = Game(window)
    
window.mainloop()