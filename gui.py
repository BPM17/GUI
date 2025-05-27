import ttkbootstrap as ttk
import tkinter as tk
import sqlite3

class Handler():
    def __init__(self, dbName):
        self.dbName = dbName
        self.conn = sqlite3.connect(f'{self.dbName}')
        self.cursor = self.conn.cursor()
    
    def GetTable(self, tableName):
        self.cursor.execute(f'''SELECT * FROM {tableName}''')
        data = self.cursor.fetchall()
        return data
    
    def GetColumn(self, tableName, column):
        self.cursor.execute(f'''SELECT {column} FROM {tableName}''')
        data = self.cursor.fetchall()
        return data

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
        self.main.mainloop()

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

    def GetNotebookPages(self):
        l = self.handler.GetColumn("ENDPOINTS", "endpointName")
        self.EditItemList(l)

    def EditItemList(self,l):
            self.notebookNames.extend(str(item).translate(str.maketrans("", "", "'(),")) for item in l)



APIconsumer("Baruch", "800x500")