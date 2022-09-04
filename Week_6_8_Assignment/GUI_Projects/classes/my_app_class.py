from tkinter import *
from tkinter import ttk
from classes.my_text_label import *

class My_App():


    def __init__(self):
        self.my_app_window = Tk()
        self.theName = StringVar()        

        # Declare list of dictionaries
        # self.empCheckBox = IntVar()
        # self.insCheckBox = IntVar()
        # self.stuCheckBox = IntVar()
        
        # # Define checkbox lables and values
        # self.checkBoxVars = [{"label":"Employee", "bindVar":self.empCheckBox}, 
        #                      {"label":"Instructor", "bindVar":self.insCheckBox},
        #                      {"label":"Student", "bindVar":self.stuCheckBox}]

        # Define List box items
        self.my_listbox = Listbox()
        self.listBoxVars = ["AL","AK","AZ", "AR", "MI", "CT",
                            "OH", "NY", "MS", "OR", "FL","TX",
                            "KS", "NJ", "WI", "WA", "WY", "ND"]


        # Define radio button labels and values
        # self.radioButtonVal = StringVar()
        # self.radioButtonItems = ["red", "blue", "green"]


        # Define Combo box items
        self.comboBoxVal = ttk.Combobox()
        self.comboBoxItems = ["red", "blue", "green"]


        self.setupInterface()

    def drawListBoxes(self):
        scrollBar = Scrollbar(self.my_app_window, orient=VERTICAL)
        scrollBar.grid(row=1, column=1, sticky=N+S+W)


        self.my_listbox = Listbox(self.my_app_window, relief=SUNKEN, yscrollcommand=scrollBar.set, selectmode=MULTIPLE)
        self.my_listbox.grid(row=1, column=0, sticky=NSEW)


        list_index = 0
        for listItem in self.listBoxVars:
            self.my_listbox.insert(list_index, listItem)
            list_index = list_index + 1

        scrollBar.config(command=self.my_listbox.yview)

    # def drawCheckBoxes(self):
    #     col_count = 0
    #     for checkBox in self.checkBoxVars:
    #         Checkbutton(self.my_app_window, text=checkBox["label"], variable=checkBox["bindVar"]).grid(row=1, column=col_count, sticky=NSEW)
    #         col_count = col_count + 1


    # def drawRadioButtons(self):
    #     col_count = 0
    #     for radioButton in self.radioButtonItems:
    #         Radiobutton(self.my_app_window, text=radioButton, variable=self.radioButtonVal, value=radioButton).grid(row=2, column=col_count, sticky=NSEW)
    #         col_count = col_count + 1

    #     self.radioButtonVal.set(self.radioButtonItems[0])

    def drawCombBox(self):
        self.comboBoxVal = ttk.Combobox(self.my_app_window, state="readonly", values=self.comboBoxItems)
        self.comboBoxVal.grid(row=2, column=0, sticky=NSEW)
        self.comboBoxVal.current(0)

    def setiupGrid(self):
        # Version 1
        # cell1_text = Text(self.my_app_window, relief=RIDGE, width=10, height=1)
        # cell1_text.grid(row=0, column=0, rowspan=2, sticky=NSEW)
        # cell1_text.insert(END, "Cell 1")
        # cell1_text.config(state=DISABLED)
        # cell2_text = Text(self.my_app_window, relief=RIDGE, width=10, height=1)
        # cell2_text.grid(row=0, column=1, sticky=NSEW)
        # cell2_text.insert(END, "Cell 2")
        # cell1_text.config(state=DISABLED)
        # cell3_text = Text(self.my_app_window, relief=RIDGE, width=10, height=1)
        # cell3_text.grid(row=1, column=1, sticky=NSEW)
        # cell3_text.insert(END, "Cell 3")
        # cell1_text.config(state=DISABLED)

        # Version 2
        # TextLabel(self.my_app_window, "Cell 1", 0, 0, 2)
        # TextLabel(self.my_app_window, "Cell 2", 0, 1)
        # TextLabel(self.my_app_window, "Cell 3", 1, 1)

        
        text_label = TextLabel(self.my_app_window, "Name", 0, 0)
        text_label.bind("<Button-1>", self.submitData)
        nameField = Entry(self.my_app_window)
        nameField.grid(row=0, column=1, sticky=NSEW)
        nameField.config(textvariable=self.theName)
        nameField.bind("<Return>", self.submitData)

        # self.drawCheckBoxes()
        self.drawListBoxes()
        # self.drawRadioButtons()
        self.drawCombBox()
        submitButton = Button(self.my_app_window, text="Submit")
        submitButton.grid(row=3, column=0, columnspan=2, sticky=NSEW)
        submitButton.bind("<Button-1>", self.submitData)

    def setupInterface(self):
        self.my_app_window.title("My App")
        self.setiupGrid()
        self.theName.set("Huma Abdul")
        self.my_app_window.mainloop()
        

    def submitData(self, *passed_args):
        # roles = ""
        # if self.empCheckBox.get() == 1:
        #     roles = roles + " Employee"
        # if self.stuCheckBox.get() == 1:
        #     roles = roles + " Student"
        # if self.insCheckBox.get() == 1:
        #     roles = roles + " Instructor"

        selectedItems = self.my_listbox.curselection()
        states = ""
        for stateIndex in selectedItems:
            states = states + " " + self.listBoxVars[stateIndex]
        # print( self.theName.get() + "**" + roles + " has a favourite color of " + self.radioButtonVal.get())
        # print( self.theName.get() + "**" + states + " has a favourite color of " + self.radioButtonVal.get())
        print( self.theName.get() + "**" + states + " has a favourite color of " + self.comboBoxVal.get())