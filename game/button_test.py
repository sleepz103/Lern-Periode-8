import tkinter as tkinter
from button import GameButton

window = tkinter.Tk()
window.title("Lights out")
window.geometry("600x400")

# testing if button is aware of it's color
# create button and add to window
bobTheButton = GameButton(window)

# print it's current color
print(bobTheButton.get_color())
# perform click
bobTheButton.click()
# print it's current color
print(bobTheButton.get_color())

# perform clicking and check color 3 times
for i in range(3):
    bobTheButton.click()
    print(bobTheButton.get_color())