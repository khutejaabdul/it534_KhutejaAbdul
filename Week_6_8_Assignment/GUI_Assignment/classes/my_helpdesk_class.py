from distutils.cmd import Command
from fileinput import filename
from lib2to3.pgen2.token import STRING
import os
import json
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from classes.label_text_style import *
from datetime import datetime

class My_Helpdesk_App():
    def __init__(self):
        self.my_app_window = Tk()
       
        self.my_app_window.geometry("500x400")

        self.my_text_box = Text()

        self.comboBoxVal = ttk.Combobox()
        self.cb_maxThreads_options  = [1,2,4]

        self.cb_event_types = ["application", "security", "error", "input/output"]

        self.cb_file_types = [".doc", ".docx", ".ppt", ".pptx", ".xls", ".mov",
                            ".xslx", ".rtf", ".pdf", ".txt", ".jpg", ".mp4",
                            ".png", ".gif", ".xml", ".html", ".zip"]

        self.cb_debugModes = ["Y", "N"]
        self.thePort = StringVar()
        self.theLocation = StringVar()
        
        self.setupInterface()

    # def drawRadioButtons(self):
    #     col_count = 0
    #     for radioButton in self.rb_debugModeItems:
    #         Radiobutton(self.my_app_window, text=radioButton, variable=self.rb_debugModeVal, value=radioButton).grid(row=6, column=col_count, sticky=NSEW)
    #         col_count = col_count + 1

    #     self.rb_debugModeVal.set(self.rb_debugModeItems[0])

    def getFile(self, *args):
        openFile = askopenfilename()
        if openFile:
            with open(openFile) as my_file:
                config_vars = json.load(my_file)
                self.comboBoxVal1 = ttk.Combobox(self.my_app_window, values=self.cb_maxThreads_options)
                self.comboBoxVal1.grid(row=1, column=3, sticky=NSEW)
                self.comboBoxVal1.current(self.cb_maxThreads_options.index(config_vars["maxThreads"]))

                locationField = Entry(self.my_app_window)
                locationField.grid(row=2, column=3, sticky=NSEW)
                locationField.config(textvariable=self.theLocation)
                self.theLocation.set(config_vars["eventLogLocation"])

                self.comboBoxVal2 = ttk.Combobox(self.my_app_window, values=self.cb_file_types)
                self.comboBoxVal2.grid(row=3, column=3, sticky=NSEW)
                self.comboBoxVal2.current(self.cb_file_types.index(config_vars["fileTypes"]))

                self.comboBoxVal3 = ttk.Combobox(self.my_app_window, values=self.cb_event_types)
                self.comboBoxVal3.grid(row=4, column=3, sticky=NSEW)
                self.comboBoxVal3.current(self.cb_event_types.index(config_vars["typesOfEvents"]))               

                self.comboBoxVal4 = ttk.Combobox(self.my_app_window, values=self.cb_debugModes)
                self.comboBoxVal4.grid(row=5, column=3, sticky=NSEW)
                self.comboBoxVal4.current(self.cb_debugModes.index(config_vars["debugMode"]))                

                nameField = Entry(self.my_app_window)
                nameField.grid(row=6, column=3, sticky=NSEW)
                nameField.config(textvariable=self.thePort)
                self.thePort.set(config_vars["serverPort"])

    # def saveFile(self, *args):

    def setiupGrid(self):
        TextLabel(self.my_app_window, "Max Threads", 1, 0)
        TextLabel(self.my_app_window, "Log Location", 2, 0)
        TextLabel(self.my_app_window, "File Types", 3, 0)
        TextLabel(self.my_app_window, "Event Types", 4, 0)
        TextLabel(self.my_app_window, "Debug Mode", 5, 0)
        TextLabel(self.my_app_window, "Server Port", 6, 0)

    
    def makeDownloadIcon(self):
        open_button = Button(self.my_app_window, text= "Download", bg="blue", font="Arial", foreground="white", command=self.getFile)
        open_button.grid(row=0, column=0, sticky=W)

    def makeUploadIcon(self):
        submitButton = Button(self.my_app_window, text="Upload", bg="blue", font="Arial", foreground="white")
        submitButton.grid(row=10, column=0, columnspan=1, sticky=NSEW)
        submitButton.bind("<Button-1>", self.submitData)

    def closeWindow(self):
        closeButton = Button(self.my_app_window, text="Close", bg="red", font="Arial", foreground="white", command=self.my_app_window.destroy)
        closeButton.grid(row=10, column=1, columnspan=1, sticky=NSEW)

    def setupInterface(self):
        self.my_app_window.title("Helpdesk Configuration Settings")
        self.setiupGrid()
        self.makeDownloadIcon()
        self.makeUploadIcon()
        self.closeWindow()
        self.my_app_window.mainloop()

    def submitData(self, *args):
        print("You have clicked on Submit button")
        print("Max Threads value is: " + self.comboBoxVal1.get())
        print("Log file location is: " + self.theLocation.get())
        print("File Type value is: " + self.comboBoxVal2.get())
        print("Event Type value is: " + self.comboBoxVal3.get())
        print("Debug Mode value is: " + self.comboBoxVal4.get())
        print("Server Port value is: " + self.thePort.get())
        self.writeToJsonFile()
       # Create a file to write this Json data to:
    #    print(json.dumps("Hello "))

    def writeToJsonFile(self, *args):
        """
            This function writes the contents of the data dictionary to a json file
            Arguments:
                Takes in any number of arguments 
            Results:
                Writes data to a Json file and gives a message
                stating so.      
        """
        data_dict = {}
        data_dict.update({"maxThreads": self.comboBoxVal1.get()})
        data_dict.update({"eventLogLocation": self.theLocation.get()})
        data_dict.update({"fileTypes": self.comboBoxVal2.get()})
        data_dict.update({"typesOfEvents": self.comboBoxVal3.get()})
        data_dict.update({"debugMode": self.comboBoxVal4.get()})
        data_dict.update({"serverPort": self.thePort.get()})

        jsonStr = json.dumps(data_dict, indent=4)
        date = datetime.now().strftime(r'%Y%m%d%H%M%S')
        fileName = f"text_files/new_config_file_{date}.json"
        
        with open(fileName, "w") as newConfigFile:            
            newConfigFile.write(jsonStr)
            print("new config settings have been writting to: "+ fileName)