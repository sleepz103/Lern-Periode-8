import tkinter
from tkinter import ttk  # tkinter.tkk is a module for modern themed widget

# window
window = tkinter.Tk()
window.title("Grid")
window.geometry("600x400")

# widgets
button1 = ttk.Button(window, text="Button 1")
button2 = ttk.Button(window, text="Button 2")
button3 = ttk.Button(window, text="Button 3")
button4 = ttk.Button(window, text="Button 4")
button5 = ttk.Button(window, text="Button 5")
button6 = ttk.Button(window, text="Button 6")
button7 = ttk.Button(window, text="Button 7")
button8 = ttk.Button(window, text="Button 8")
button9 = ttk.Button(window, text="Button 9")


# define a grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

# buttons
button1.grid(row=0, column=0, sticky="nesw")
button2.grid(row=0, column=1, sticky="nesw")
button3.grid(row=0, column=2, sticky="nesw")
button4.grid(row=1, column=0, sticky="nesw")
button5.grid(row=1, column=1, sticky="nesw")
button6.grid(row=1, column=2, sticky="nesw")
button7.grid(row=2, column=0, sticky="nesw")
button8.grid(row=2, column=1, sticky="nesw")
button9.grid(row=2, column=2, sticky="nesw")





# run
window.mainloop()
