import ttkbootstrap as ttk
import tkinter as tk
import sqlite3
from SQLiteHandler import Handler

class Main(ttk.Window):
    def __init__(self, title, dimensions):
        super().__init__(self)
        self.title(title)
        self.geometry(dimensions)

    def __str__(self):
        return super().__str__()

class APIconsumer():
    def __init__(self,title, dimensions):
        self.main = Main(title, dimensions)
        self.handler = Handler("C:\API\API\ApiDb.db")   
        self.notebookFrames = []
        self.notebookNames = []
        self.mainFrame = self.CreateMainFrame(self.main, "750x450")
        self.CreateContentWindow()
        self.notebook.bind("<<NotebookTabChanged>>", self.OnTabChanged)
        self.DisplayOnTab()
        self.main.mainloop()

    def DisplayOnTab(self):
        pass

    def CreateMainFrame(self, parent, dimensions):
        dimensions  = dimensions.split('x')
        width = dimensions[0]
        height = dimensions[1]
        frame = ttk.Frame(parent, height=height, width=width)
        frame.place(x=40, y=25, relwidth=0.9, relheight=0.9)
        return frame
    
    def CreateContentWindow(self):
        self.GetNotebookPages()
        self.notebook = ttk.Notebook(self.main)
        for i in range(len(self.notebookNames)):
            self.notebookFrames.append(ttk.Frame(self.notebook))
            self.notebook.add(self.notebookFrames[i], text=self.notebookNames[i])
        self.notebook.pack()
    
    def OnTabChanged(self, event):
        n = event.widget
        index = self.notebook.index("current")
        self.currentTab = (self.notebook.tab(index,"text")).replace(" ", "").lower()
        
        print(self.currentTab)

    def GetNotebookPages(self):
        l = self.handler.GetColumn("ENDPOINTS", "endpointName")
        self.EditItemList(l)

    def EditItemList(self,l):
        self.notebookNames.extend(str(item).translate(str.maketrans("", "", "'(),")) for item in l)

    def GetEndpointsFields(self):
        h = Handler("C:\GUI\GUI\guiDb.db")
        l = h.GetRegister("EndpointsFields", "putcar")

    def GetCurrentTab(self):
        index = self.notebook.index('current')
        print(index)

APIconsumer("Baruch", "800x500")