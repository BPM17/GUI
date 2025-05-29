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
    
    def CreateDb(self):
        try:
            self.conn = sqlite3.connect(self.dbName, check_same_thread=False)
            print("Connection Stablished")
        except:
            print("Something went wrong")
    
    def CreateTable(self, command):
        self.cursor.execute(command)

    def GetColumn(self, tableName, column):
        self.cursor.execute(f'''SELECT {column} FROM {tableName}''')
        data = self.cursor.fetchall()
        return data
    
    def Pragma(self):
        self.cursor.execute(f'''PRAGMA automatic_index''')
        data = self.cursor.fetchall()
        for i in data:
            print(i)

    def GetRegister(self, tableName, identifier):
        self.cursor.execute(f'''SELECT * FROM {tableName} WHERE endpoint = '{identifier}';''')
        return self.cursor.fetchall()

if __name__ == "__main__":
    dbName = "C:\GUI\GUI\guiDb.db"
    command = '''CREATE TABLE IF NOT EXISTS Layout(
    id INTEGER PRIMARY KEY,
    Window VARCHAR(50) NOT NULL,
    label INTEGER NOT NULL,
    entry INTEGER NOT NULL,
    button INTEGER NOT NULL
    )'''
    db = Handler(dbName)
    # data = db.GetTable("Endpoints")
    # print(data)
    db.CreateDb()
    db.CreateTable(command)