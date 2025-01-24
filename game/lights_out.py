import tkinter as tkinter
from button import GameButton

window = tkinter.Tk()
window.title("Lights out")
window.geometry("600x400")


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