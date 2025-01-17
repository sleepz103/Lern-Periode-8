import tkinter as tkinter
from itertools import cycle

window = tkinter.Tk()
window.title("automated grid")
window.geometry("600x400")

colors = "red", "green", "blue", "orange", "purple"

class GameButton(tkinter.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(command=self.click_function)
        self.color = cycle(colors)
    def click_function(self):
        new_color = next(self.color)
        self.config(background=new_color, activebackground=new_color)

for i in range(0,3):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

buttons = []
for row in range(0,3):
    row_buttons = []
    for col in range(0,3):
        button = tkinter.Button(window)
        gameButton = GameButton(button)
        button.grid(row=row, column=col, sticky='nesw')
        row_buttons.append(gameButton)
    buttons.append(row_buttons)


def main():
    root = tkinter.Tk()
    for i in range(10):
        btn = GameButton(root, text=f"Button number {i}")
        btn.pack()
    root.mainloop()

if __name__ == '__main__':
    main()