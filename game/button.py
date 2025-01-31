import tkinter as tkinter

class GameButton(tkinter.Button):
    def __init__(self, x_pos, y_pos, *args, **kwargs):
        kwargs["background"] = kwargs.get("background", "black")
        kwargs["activebackground"] = kwargs.get("activebackground", "black")
        super().__init__(*args, **kwargs)
        self.config(command=self.click)
        self.color = "black"
        self.is_active = False
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.config(text = "{}x,{}y".format(self.x_pos,self.y_pos))
        
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def get_state(self):
        return self.is_active
    
    def set_state(self, state):
        self.is_active = state

    
    def toggle_state(self):
        if self.is_active:
            self.set_color("black")
            self.set_state(False)
        else:
            self.set_color("red")
            self.set_state(True)
    
    def click(self):
        self.toggle_state()
        self.config(background=self.get_color(), activebackground=self.get_color())
