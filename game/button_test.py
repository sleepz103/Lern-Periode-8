import tkinter as tkinter
from button import GameButton

window = tkinter.Tk()
window.title("Lights out")
window.geometry("600x400")


bobTheButton = GameButton(window)

print(bobTheButton.get_color())

bobTheButton.click()

print(bobTheButton.get_color())

for i in range(3):
    bobTheButton.click()
    print(bobTheButton.get_color())