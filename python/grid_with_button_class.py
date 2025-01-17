import tkinter as tkinter
import random

window = tkinter.Tk()
window.title("automated grid")
window.geometry("600x400")

colors = ("red", "green", "blue", "orange", "purple")

class GameButton(tkinter.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(command=self.click_function)
        self.color = random.choice(colors)
    def click_function(self):
        new_color = random.choice(colors)
        self.config(background=new_color, activebackground=new_color)

for i in range(0,3):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

buttons = []
for row in range(0,3):
    row_buttons = []
    for col in range(0,3):
        gameButton = GameButton(window)
        gameButton.grid(row=row, column=col, sticky='nesw')
        row_buttons.append(gameButton)
    buttons.append(row_buttons)

window.mainloop()