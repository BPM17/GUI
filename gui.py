import ttkbootstrap as ttk
import tkinter as tk
import sqlite3
from SQLiteHandler import Handler
from requester import Requester
import json
from pprint import pprint

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
        self.currentTab = ''
        self.fields=''
        self.endpoints = []
        self.labels = []
        self.entries = []
        self.buttons = []
        self.requester = Requester
        self.mainFrame = self.CreateMainFrame(self.main, "750x450")
        self.CreateContentWindow()
        self.notebook.bind("<<NotebookTabChanged>>", self.OnTabChanged)
        self.main.mainloop()

    def DisplayOnTab(self):
        self.fields = self.GetEndpointsFields()
        self.PackFields()
        self.GridkButtons()

    def CheckEmptyFields(self):
        pass

    def Execute(self):
        payload ={}
        headers = {
            'Content-Type': 'application/json'
            }
        if len(self.fields) == 1 and len(self.entries) == 0:
            response = self.requester.Get("GET", f"{self.currentTab}/", "", payload)
            response = json.loads(response)
            response = self.Prettyfy(response)
            self.labels[0].config(text = response)
        elif len(self.fields) == 1 and len(self.entries) == 1:
            response = self.requester.Get("GET", f"{self.currentTab}/{self.entries[0].get()}", "", payload)
            response = json.loads(response)
            response = self.Prettyfy(response)
            self.labels[1].config(text = response)
        else:
            for i in range(len(self.fields)):
                payload [f"{self.fields[i]}"] = f"{self.entries[i].get()}"
            payload = json.dumps(payload)
            response = self.requester.Put("PUT", f"{self.currentTab}", headers, payload)
            response = json.loads(response)
            response = self.Prettyfy(response)
            self.labels[1].config(text = response)

    def Prettyfy(self, response):
        word = ""
        if type(response) == list:
            for i in response:
                for j in i:
                    word = word + str(j) + "\n"
                word = word + "\n"
        elif type(response) == dict:
            for j in response:
                response = str(response) + "\n"
        # print(word)
        return word

    def GridkButtons(self):
        self.buttonsFrame = ttk.Frame(self.main)
        self.buttonsFrame.pack(pady=5)
        self.buttonsFrame.rowconfigure(1, weight=1)
        self.buttonsFrame.columnconfigure(4, weight=1)
        self.buttons.append(ttk.Button(self.buttonsFrame, text="Clear"))
        self.buttons[0].grid(column = 2, row = 1, sticky = tk.EW, padx = 5, pady = 5)
        self.buttons.append(ttk.Button(self.buttonsFrame, text="Execute", command= self.Execute))
        self.buttons[1].grid(column = 3, row = 1, sticky = tk.EW, padx = 5, pady = 5)

    def PackFields(self):
        self.DestroyAll()
        self.fields = list(self.fields)
        for i in range(self.notebook.index("end")):
            if self.notebook.tab(i, "text") == self.currentTab:
                for j in range(len(self.fields)):
                    if len(self.fields) != 0 and len(self.fields[0])>0:
                        self.labels.append( ttk.Label(self.notebookFrames[i],text=f"{self.fields[j]}"))
                        self.labels[j].pack(pady = 10, padx = 10)
                        self.entries.append(ttk.Entry(self.notebookFrames[i]))
                        self.entries[j].pack()
                    else:
                        self.labels.append( ttk.Label(self.notebookFrames[i],text=f"", font=('Courier', 12), justify='left'))
                        self.labels[j].pack(pady = 10, padx = 10)
                if len(self.fields) != 0 and len(self.fields[0])>0:
                    self.labels.append( ttk.Label(self.notebookFrames[i], anchor=tk.CENTER, width=100))
                    self.labels[j+1].pack(pady = 10, padx = 10)

# TODO: work distributing the fields in two columns
    def GridFields(self):
        self.DestroyAll()
        self.fields = list(self.fields)
        for i in range(self.notebook.index("end")):
            if self.notebook.tab(i, "text") == self.currentTab:
                if len(self.fields) % 2 == 0: #this means the len is multiple of two 
                    if len(self.fields) != 0 and len(self.fields[0])>0:
                            for j in range(len(self.fields)/2):
                                self.labels.append( ttk.Label(self.notebookFrames[i],text=f"{self.fields[j]}"))
                                self.labels[j].grid(column = 0, row = j, sticky = tk.EW, padx = 5, pady = 5)
                                self.entries.append(ttk.Entry(self.notebookFrames[i]))
                                self.entries[j].grid(column = 0, row = j, sticky = tk.EW, padx = 5, pady = 5)
                    else:
                        self.labels.append( ttk.Label(self.notebookFrames[i],text=f""))
                        self.labels[j].pack(pady = 10, padx = 10)
                else:
                    if len(self.fields) != 0 and len(self.fields[0])>0:
                        for j in range((len(self.fields)+1)/2):
                            self.labels.append( ttk.Label(self.notebookFrames[i],text=f"{self.fields[j]}"))
                            self.labels[j].grid(column = 0, row = j, sticky = tk.EW, padx = 5, pady = 5)
                            self.entries.append(ttk.Entry(self.notebookFrames[i]))
                            self.entries[j].grid(column = 0, row = j, sticky = tk.EW, padx = 5, pady = 5)



    def DestroyAll(self):
        for i in self.labels:
            i.destroy()
        for i in self.entries:
            i.destroy()
        self.labels.clear()
        self.entries.clear()

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
            self.notebookFrames.append(ttk.Frame(self.notebook, width = 500, height = 400))
            self.notebook.add(self.notebookFrames[i], text=self.notebookNames[i])
        self.notebook.pack(pady=10, padx=10, fill='both', expand=True)
    
    def OnTabChanged(self, event):
        n = event.widget
        index = self.notebook.index("current")
        self.currentTab = (self.notebook.tab(index,"text")).replace(" ", "").lower()
        self.DisplayOnTab()

    def GetNotebookPages(self):
        self.endpoints = self.handler.GetColumn("ENDPOINTS", "endpointName")
        self.EditItemList(self.endpoints)

    def EditItemList(self,l):
        self.notebookNames.extend(str(item).translate(str.maketrans("", "", "'(),")) for item in l)

    def GetEndpointsFields(self):
        h = Handler("C:\GUI\GUI\guiDb.db")
        l = h.GetRegister(f"EndpointsFields", self.currentTab)
        l = l[0][-1].strip("[]").replace(" ", "")
        l = l.split(",")
        return(l)


APIconsumer("Baruch", "800x500")