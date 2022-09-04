import os
from tkinter import *

class My_Menu():


    def __init__(self):
        self.my_app_window = Tk()
        print(os.getcwd())
        self.my_app_window.geometry("700x450")
        self.openIconImage = PhotoImage(file="images/folder_open_icon.png")

        self.setupInterface()

    def configureApp(self, *args):
        print("configureApp method called")

    def drawCircle(self, *args):
        print("drawCircle method called")

    def drawDashedLine(self, *args):
        print("drawDashedLine method called")

    def drawLine(self, *args):
        print("drawLine method called")

    def drawSquare(self, *args):
        print("drawSquare method called")

    def editPreferences(self, *args):
        print("editPreferences method called")

    def getFile(self, *args):
        print("GetFile method called")

    def makeIconMenu(self):
        open_button = Button(self.my_app_window, command=self.getFile)
        open_button.config(image=self.openIconImage, width=81, height=77)
        open_button.grid(row=0, column=0, sticky=W)

    def setupMenu(self):
        topMenu = Menu(self.my_app_window)
        self.my_app_window.config(menu=topMenu)

        draw = Menu(topMenu)
        draw.add_command(label="Draw Circle", command=self.drawCircle, accelerator="Ctrl+d")
        draw.add_command(label="Draw Square", command=self.drawSquare, accelerator="Ctrl+b")
        topMenu.add_cascade(label="Draw", menu=draw)

        lineMenu = Menu(draw)
        lineMenu.add_command(label="Draw Regular Line", command=self.drawLine, accelerator="Ctrl+l")
        lineMenu.add_command(label="Draw Dashed Line", command=self.drawDashedLine, accelerator="Ctrl+i")
        draw.add_cascade(label="Line Options", menu=lineMenu)

        configure = Menu(topMenu)
        configure.add_command(label="Configure App", command=self.configureApp)
        configure.add_command(label="Edit Preferences", command=self.editPreferences)
        topMenu.add_cascade(label="Configuration", menu=configure)

        self.my_app_window.bind_all("<Control-d>", self.drawCircle)
        self.my_app_window.bind_all("<Control-b>", self.drawSquare)
        self.my_app_window.bind_all("<Control-l>", self.drawLine)
        self.my_app_window.bind_all("<Control-i>", self.drawDashedLine)


    def setupInterface(self):
        self.my_app_window.title("My App")
        self.setupMenu()
        self.makeIconMenu()
        self.my_app_window.mainloop()