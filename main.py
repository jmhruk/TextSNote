import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename
from tkinter.messagebox import askyesno
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Notebook
import tkinter.font as tkFont
import re

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title('TextS Note')
        self.geometry("600x300")
        
        self.resizable(False, False)

        self.backGroundI=PhotoImage(file="bg2.png")
        self.backGround=Label(self,image=self.backGroundI)
        self.backGround.place(x=0, y=0)

        self.loadimage = tk.PhotoImage(file="crpg.png")

        self.cButton = Button(self, command=self.createPage, image=self.loadimage)
        self.cButton["bg"] = "white"
        self.cButton["border"] = 0
        self.cButton["borderwidth"] = 8
        self.cButton["relief"] = "solid"
        self.cButton.place(x=145, y=155)


            #file menu
        self.createMenu()
        self.createTopFrame()
        self.createMainFrame()
        self.createNotebook()
        
    def createMenu(self):

        self.menubar = Menu(self)
        self.config(menu=self.menubar)

        return

    def createPage(self):
        
        helv18 = tkFont.Font(family="Helvetica",size=18,weight="normal")

        top = Toplevel(self)
        top.geometry("200x100")
        top.configure(bg="gray")


        lab = Label(top, text="Enter a tab name:")
        lab.place(x=60, y=0)

        entry = Entry(top, width=100)
        entry.place(y=30)

        n = self.notebook


    def createTopFrame(self):
        self.topFrame = Frame(self, width=600, height=100)
        self.topFrame.place(x=0, y=0)
        
        self.backGroundImage=PhotoImage(file="background.png")
        self.backGroundImageLabel=Label(self.topFrame,image=self.backGroundImage)
        self.backGroundImageLabel.place(x=0, y=0)

        ml_font = tkFont.Font(family="Helvetica",size=35,weight="bold")


        self.mlabel = Label(self.topFrame,text="TextS Note", font=ml_font, bd=5, bg="lightblue", borderwidth=3, relief="solid")
        self.mlabel.place(x=185, y=20)
        

        




    def createMainFrame(self):
        self.mainFrame = Frame(self)
        self.mainFrame.grid(row=2, column=0)

    def createNotebook(self):
        self.notebook = Notebook(self.mainFrame)
        self.notebook.grid(row=0, column=0)
        

app = App()

app.mainloop()