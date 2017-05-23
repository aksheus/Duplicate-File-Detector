from tkinter import filedialog
import tkinter
class Menu:

    def __init__(self,Title,Resolution,):
        self.Root=tkinter.Tk()
        self.Root.title(Title)
        self.Root.geometry(Resolution)
        self.MenuTitle = tkinter.Label(self.Root, text="Choose One",width=25,font=('Consolas',16))
        self.MenuTitle.pack()
        self.MenuTitle.place(x=125,y=50)
        self.Root.configure(background="black")
        self.Buttons=[]
        self.ButtonPositions=[225,150]
        self.ChosenPath=''
        self.ChosenFile=''
        self.AddButton(Text="Search All Duplicates",Action= lambda: print('all'))
        self.AddButton(Text="Find Duplicate of File",Action=lambda: print('one'))

    def GetSearchPath(self):
        self.ChosenPath=filedialog.askdirectory(parent=self.Root,initialdir="/",title="Please select base directory")
        # add validation code then return 

    def AddButton(self,Text,Action=None):
        self.Buttons.append(tkinter.Button(self.Root,text=Text,command=Action))
        self.Buttons[-1].pack()
        self.Buttons[-1].place(x=self.ButtonPositions[0],y=self.ButtonPositions[1])
        self.ButtonPositions[1]+=60





