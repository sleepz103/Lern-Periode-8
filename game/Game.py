import tkinter as tkinter
from tkinter import *
from button import GameButton

class GameSpace():
    def __init__(self, master, grid_size=3, *args, **kwargs):
        self.master = master
        self.grid_size = grid_size
        self.gridDict = {}
        self.buttons = []
        self.gameBox = tkinkter.Frane(self.master)
        self.gameBox.grid(row=0,column=1,sticky="nesw")
        self.generate_grid()

    def generate_grid(self):
        for widget in self.gameBox.winfo_children():
            widget.destroy()
        self.gameCells = {}
        self.buttons = []

        for row in range(self.grid_size):
            row_buttons = []
            for col in range(self.grid_size):
                gameButton = GameButton(row, col, self.gridDict, self.gameBox) #master=self.gameBox
                gameButton.grid(row=row, column=col, sticky='nesw')
                row_buttons.append(gameButton)
                self.gridDict[(row, col)] = gameButton
            self.buttons.append(row_buttons)
        
        for i in range(self.gridSize):
            self.gameBox.grid_rowconfigure(i, weight=1)
            self.gameBox.grid_columnconfigure(i, weight=1)
        
        