from tkinter import filedialog,messagebox
from builtins import str
import tkinter
import os 
class Menu:

    def __init__(self,Title,Resolution,):
        self.Root=tkinter.Tk()
        self.Root.title(Title)
        self.Root.geometry(Resolution)
        self.MenuTitle = tkinter.Label(self.Root, text="Find Duplicate Files",width=25,font=('Consolas',16))
        self.MenuTitle.pack()
        self.MenuTitle.place(x=125,y=50)
        self.Root.configure(background="black")
        self.Buttons=[]
        self.ButtonPositions=[225,150]
        self.ChosenPath=''
        self.ChosenFile=''
        self.IsSingle=False
        self.SetupButtons()
        self.Root.mainloop()

    def GetSearchPath(self,IsSingle):
        self.ChosenPath=filedialog.askdirectory(parent=self.Root,initialdir="/",title="Please select base directory")
        assert isinstance(self.ChosenPath,str)
        if not os.path.exists(self.ChosenPath):
            messagebox.showerror('Error','Path Does not Exist')
            self.Root.destroy()
        if IsSingle:
            self.ChosenFile=filedialog.askopenfilename(parent=self.Root,title='Choose a File')
            assert isinstance(self.ChosenFile,str)
            if not os.path.exists(self.ChosenFile):
                messagebox.showerror('Error','File Does Not Exist')
                self.Root.destroy()
            self.IsSingle=True
        messagebox.showinfo('Execution','Csv of Duplicate Files Will Be Generated Shortly')
        self.Root.destroy()
        return 


    def AddButton(self,Text,Action=None):
        self.Buttons.append(tkinter.Button(self.Root,text=Text,command=Action))
        self.Buttons[-1].pack()
        self.Buttons[-1].place(x=self.ButtonPositions[0],y=self.ButtonPositions[1])
        self.ButtonPositions[1]+=60
        return

    def SetupButtons(self):
        self.AddButton(Text="Search All Duplicates",Action= lambda : self.GetSearchPath(False))
        self.AddButton(Text="Find Duplicate of File",Action= lambda : self.GetSearchPath(True))
        return

