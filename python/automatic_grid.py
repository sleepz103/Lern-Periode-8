import tkinter as tkinter

window = tkinter.Tk()
window.title("automated grid")
window.geometry("600x400")

for i in range(0, 3):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

buttons = []
for row in range(0, 3):
    row_buttons = []
    for col in range(0, 3):
        button = tkinter.Button(window)
        button.grid(row=row, column=col, sticky='nesw')
        row_buttons.append(button)
    buttons.append(row_buttons)



window.mainloop()
