from tkinter import *

class TextLabel(Text):

    def __init__(self, passed_window=None, passed_labelText= "",
                passed_row=0, passed_column=0, passed_columnspan=2, passed_sticky=NSEW):
        Text.__init__(self, passed_window, relief=RIDGE, width=20, height=1)
        self.grid(row=passed_row, column=passed_column, columnspan=passed_columnspan, sticky=passed_sticky)
        self.insert(END, passed_labelText)
        self.config(state=DISABLED, bg="white", foreground="black")