import os
import sys
import shutil
import string
import tkinter
from tkinter import filedialog


class Application(tkinter.Frame): ##Main application
    FileTypes =[]
    def MENU_BAR(self):
        self.BAR = tkinter.Menu()
        def mkshow(menu, entry):
            def emit():
                if entry == 'New Search':
                    self.TEXT.delete('1.0','3.0')
                if entry == 'Exit':
                    self.quit()
            return emit

        self.FILE = tkinter.Menu()
        for x in 'New Search', 'Exit':
            self.FILE.add_command(label = x, command=mkshow('File',x))
        self.BAR.add_cascade(label= 'File', menu=self.FILE)

        root.config(menu=self.BAR)
        
    def File_Exts(self):                
        Ext_Lib = 'C:\Documents and Settings\jjohnston\My Documents\File_Types.txt'
        if not os.path.isfile(Ext_Lib):
            self.File_Types = ['.txt', '.xls', '.xlsx', '.dwg', '.pdf', '.ppt', '.bak', '.c', '.mp3', '.mpeg', '.avi', '.pyc', '.pptx', '.jpg', '.bmp', '.gif', '.doc', '.docx', '.sldprt', '.sldasm', '.stp', '.step', '.slddrw', '.py']
            self.File_Types.sort(cmp=cmp,key=None, reverse=False)
            Archive = open(Ext_Lib, 'w')
            print >>Archive, self.File_Types

        if os.path.isfile(Ext_Lib):
            Archive = open(Ext_Lib, 'r')
            File_Types = Archive.read()

        Archive.close()
        return self.File_Types

    Files1 = []
    
    Count = 0
    
    Count2 = 0
    
##    def Move_by_file_type(File_Types):
##        for

    def Folder_Selection_1(self):
        global Dir1
        Dir1 = filedialog.askdirectory()
        return Dir1

    def Folder_Selection_2(self):
        global Dir2
        Dir2 = filedialog.askdirectory()
        return Dir2

    def File_Move(self):
        Files0 = os.listdir(Dir1)

        for n in Files0:
            n2=os.path.splitext(n)
            for ext in n2:
                ext = string.lower(ext)
            for fil in self.File_Types:
                if ext == fil:
                    self.Files1.append(n)
                    Count2 = Count2 + 1
        print(self.Files1)

        for n3 in self.Files1:
            Mover = os.path.join(Dir1, n3)
            shutil.move(Mover, Dir2)
            Count = Count + 1

        print('Total Files Found:' + str(Count2))
        print ('Total Files Moved:' +  str(Count))

    def createWidgets(self):
        self.TEXT = tkinter.Text(self)
        self.TEXT.pack()

        self.QUIT = tkinter.Button(self)
        self.QUIT["text"] = "EXIT"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "bottom"})

        self.Select = tkinter.Button(self)
##        if Dir1 == None:
##            Button_Text_1 = "Select Search Folder"
##        else:
##            Button_Text_1 = Dir1
            
        self.Select["text"] = "Select Search Folder"
        self.Select["command"] = self.Folder_Selection_1
        self.Select.pack({"side": "left"})

        self.Select = tkinter.Button(self)
        self.Select["text"] = "Select Destination Folder"
        self.Select["command"] = self.Folder_Selection_2
        self.Select.pack({"side": "left"})

        self.Select = tkinter.Button(self)
        self.Select["text"] = "Move Files"
        self.Select["command"] = self.File_Move
        self.Select.pack({"side": "left"})
        

    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.MENU_BAR()

root=tkinter.Tk()
root.title("File Sorter")
app = Application(master=root)
app.mainloop()
try:
    root.destroy()
except:
    pass
