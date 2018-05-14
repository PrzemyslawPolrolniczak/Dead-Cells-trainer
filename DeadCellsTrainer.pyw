from tkinter import *
from tkinter import ttk, messagebox
import sys
from ReadWriteMemory import rwm

class Trainer:
    def __init__(self, parent):
        def about():
            messagebox.showinfo("About", "This trainer was made by Error404. Have fun")
            pass
        
        def stopTime():
            pass
        
        def addCells():
            try:
                self.addedCells = self.entryCells.get()
                if self.addedCells.strip() == '':
                    pass
                else:
                    rwm.WriteProcessMemory(self.hProcess, self.cellsVar, int(self.addedCells))
                    # print(self.entryCells.get())
                    # print(self.cellsVar)                
                    # print(self.cells)
                    # print(self.addedCells)
                    self.entryCells.delete(0, END)
            except AttributeError:
                self.entryCells.delete(0, END)

        def addGold():
            try:
                self.addedGold = self.gold + int(self.entryGold.get())
                #rwm.WriteProcessMemory(self.hProcess, self.goldVar, self.addedGold)
                self.entryGold.delete(0, END)
            except AttributeError:
                self.entryGold.delete(0, END)
                        
        def infHealth():
            pass

        def Timer():
            ProcID = rwm.GetProcessIdByName('deadcells.exe')
            self.hProcess = rwm.OpenProcess(ProcID)
            if self.hProcess == None:
                self.pLabel.config(text='Game not started')
            else:
                self.cellsVar = rwm.getPointer(self.hProcess, 0x00008db4, offsets=[0x270,0xb0,0xab4])
                self.goldVar = 0x000 #rwm.getPointer(self.hProcess, 0x000fd214, offsets=[0x30c,0x127c,0x4f4])
                # self.goldVar = rwm.getPointer(self.hProcess, 0x00008db4, offsets=[0xd0,0xc0,0x1a4])            
                
                #0c1be060
                #140a4908


                self.pLabel.config(text="Game is running", fg="green")
                self.time = rwm.ReadProcessMemory(self.hProcess, self.timeVar)
                self.showTime.config(text=self.time)

                self.gold = rwm.ReadProcessMemory(self.hProcess, self.goldVar)
                self.showGold.config(text=self.gold)

                self.cells = rwm.ReadProcessMemory(self.hProcess, self.cellsVar)
                self.showCells.config(text=self.cells)

                if self.infHealthVar == True:
                    rwm.WriteProcessMemory(self.hProcess, self.healthVar, 100)
        parent.after(100, Timer)

        #Address Variable
        self.hProcess = rwm.OpenProcess('deadcells.exe')
        
        self.timeVar = 0x000
        self.stopTimeVar = False
        
        self.healthVar = 0x000
        self.infHealthVar = False

        #Labels
        self.pLabel = Label(parent, text="Game not started", font=('Microsoft Sans Serif', 16), bg="black", fg="red")
        self.pLabel.place(x=12, y=9)
        self.timeLabel = Label(parent, text="Time:", font=('Microsoft Sans Serif', 16), bg="black", fg="white")
        self.timeLabel.place(x=12, y=51)
        self.showTime = Label(parent, text="00:00:00", font=('Microsoft Sans Serif', 16), bg="black", fg="white")
        self.showTime.place(x=70, y=51)
        self.cellsLabel = Label(parent, text="Cells:", font=('Microsoft Sans Serif', 16), bg="black", fg="white")
        self.cellsLabel.place(x=12, y=93)
        self.showCells = Label(parent, text="0", font=('Microsoft Sans Serif', 16), bg="black", fg="white")
        self.showCells.place(x=70, y=93)
        self.goldLabel = Label(parent, text="Gold:", font=('Microsoft Sans Serif', 16), bg="black", fg="white")
        self.goldLabel.place(x=12, y=135)
        self.showGold = Label(parent, text="0", font=('Microsoft Sans Serif', 16), bg="black", fg="white")
        self.showGold.place(x=70, y=135)

        #Buttons
        self.freezeButton = ttk.Button(parent, text="Freeze time", command=stopTime)
        self.freezeButton.place(w=115,h=25,x=325,y=55)
        self.aboutButton = ttk.Button(parent, text="About", command = about)
        self.aboutButton.place(x=365, y=9)
        self.cellsButton = ttk.Button(parent, text="Add", command = addCells)
        self.cellsButton.place(x=365, y=93)
        self.goldButton = ttk.Button(parent, text="Add", command = addGold)
        self.goldButton.place(x=365, y=133)

        #Entries
        self.entryCells = ttk.Entry(parent)
        self.entryCells.place(w=50,x=310, y=95)
        self.entryGold = ttk.Entry(parent)
        self.entryGold.place(w=50,x=310, y=135)
        Timer()

def main():
    root = Tk()
    wFilter = 457; hFilter = 455
    w = wFilter - 8; h = hFilter - 47
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    root.title('Dead Cells Trainer by Error404')
    root.configure(background='#000')
    test = StringVar()
    # a = ttk.Entry(root, width=7, textvariable=test)        
    # a.pack()
    MainWindow = Trainer(root)

    root.mainloop()
    sys.exit(1)
main()