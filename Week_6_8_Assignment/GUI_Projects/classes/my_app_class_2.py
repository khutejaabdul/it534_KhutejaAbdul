
from cgi import test
from tkinter import *
from classes.my_text_label import *

class My_App():


    def __init__(self):
        self.my_app_window = Tk()
        self.setupInterface()


    def setiupGrid(self):
        TextLabel(self.my_app_window, "Name", 0, 0)
        NameFiled = Entry(self.my_app_window)
        NameFiled.grid(row=0, column=1, sticky=NSEW)

        submitButton = Button(self.my_app_window, text="Submit")
        submitButton.grid(row=1, column=0, columnspan=2, sticky=NSEW)

    def setupInterface(self):
        self.my_app_window.title("My App")
        self.setiupGrid()
        self.my_app_window.mainloop()
        