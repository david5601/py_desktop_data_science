from tkinter import ttk
import tkinter as tk

class AssignPendingApp(tk.Tk):
    def __init__(self, data):
        super().__init__()

        self.title("AssignPendingList")
        self.geometry("875x150")
        self.resizable(False, False)

        self.style = ttk.Style()
        # self.style.configure("TLabel", font=("ROBOTO", 13, "bold"), background="white", anchor="center", justify="center")
        self.style.configure("Custom.TButton", font=("ROBOTO", 13, "bold"))
        # s = ttk.Style()
        # s.configure('W.TButton', font =('calibri', 10, 'bold', 'underline'))

        self.buttonPrevious = ttk.Button(self, text="Previous", command=self.PreviousPendingList, style="Custom.TButton")
        # self.buttonPrevious.configure()
        self.buttonPrevious.place(x=20, y=60)

        self.labelNumber = ttk.Label(self, text="", width=2, font=("ROBOTO", 13, "bold"), background="white", anchor="center", justify="center")
        self.labelNumber.config(borderwidth=2, relief="solid")
        self.labelNumber.place(x=110, y=61)

        self.labelFirstName = ttk.Label(self, text="", width=10, font=("ROBOTO", 13, "bold"), background="white", anchor="center", justify="center")
        self.labelFirstName.config(borderwidth=2, relief="solid")
        self.labelFirstName.place(x=140, y=61)

        self.labelLastName = ttk.Label(self, text="", width=21, font=("ROBOTO", 13, "bold"), background="white", anchor="center", justify="center")
        self.labelLastName.config(borderwidth=2, relief="solid")
        self.labelLastName.place(x=243, y=61)

        self.labelInmateID = ttk.Label(self, text="", width=10, font=("ROBOTO", 13, "bold"), background="white", anchor="center", justify="center")
        self.labelInmateID.config(borderwidth=2, relief="solid")
        self.labelInmateID.place(x=445, y=61)   

        self.labelPIN = ttk.Label(self, text="", width=14, font=("ROBOTO", 13, "bold"), background="white", anchor="center", justify="center")
        self.labelPIN.config(borderwidth=2, relief="solid")
        self.labelPIN.place(x=550, y=61)

        self.buttonNext = ttk.Button(self, text="Next", command=self.NextPendingList)
        self.buttonNext.place(x=695, y=60)

        self.buttonCopy = ttk.Button(self, text="Copy", command=self.CopyPendingData)
        self.buttonCopy.place(x=780, y=60)

        self.currentIndex = 0
        self.pendingList = data

        self.LoadInitState()

    def LabelClear(self):
        self.labelNumber.configure(text="")
        self.labelFirstName.configure(text="")
        self.labelLastName.configure(text="")
        self.labelInmateID.configure(text="")
        self.labelPIN.configure(text="")

    def LoadInitState(self):
        # self.LabelClear()
        self.currentIndex = 0

        self.labelNumber.configure(text=str(int(self.currentIndex + 1)))
        self.labelFirstName.configure(text=str(self.pendingList[self.currentIndex][0]))
        self.labelLastName.configure(text=str(self.pendingList[self.currentIndex][1]))
        self.labelInmateID.configure(text=self.StringIDNumberMatch(self.pendingList[self.currentIndex][2]))
        self.labelPIN.configure(text=self.StringPINNumberMatch(self.pendingList[self.currentIndex][3]))


    def PreviousPendingList(self):
        if self.currentIndex >= 1:
            self.LabelClear()
            self.currentIndex = self.currentIndex - 1
        
            self.labelNumber.configure(text=str(int(self.currentIndex + 1)))
            self.labelFirstName.configure(text=str(self.pendingList[self.currentIndex][0]))
            self.labelLastName.configure(text=str(self.pendingList[self.currentIndex][1]))
            self.labelInmateID.configure(text=self.StringIDNumberMatch(self.pendingList[self.currentIndex][2]))
            self.labelPIN.configure(text=self.StringPINNumberMatch(self.pendingList[self.currentIndex][3]))

    def NextPendingList(self):
        if self.currentIndex < len(self.pendingList) - 1:
            self.LabelClear()
            self.currentIndex = self.currentIndex + 1

            self.labelNumber.configure(text=str(int(self.currentIndex + 1)))
            self.labelFirstName.configure(text=str(self.pendingList[self.currentIndex][0]))
            self.labelLastName.configure(text=str(self.pendingList[self.currentIndex][1]))
            self.labelInmateID.configure(text=self.StringIDNumberMatch(self.pendingList[self.currentIndex][2]))
            self.labelPIN.configure(text=self.StringPINNumberMatch(self.pendingList[self.currentIndex][3]))

    def CopyPendingData(self):
        self.clipboard_clear()
        self.clipboard_append(self.pendingList[int(self.currentIndex)][2])
        self.update()
        self.NextPendingList()

    def StringIDNumberMatch(self, s):
        shortNum = int(s)
        midString = str(int(s))
        cnt = 0

        while shortNum > 0:
            shortNum = int(shortNum / 10)
            cnt += 1
    
        for i in range(7 - cnt):
            midString = str(int(0)) + midString
        
        return midString 
    
    def StringPINNumberMatch(self, s):
        shortNum = int(s)
        midString = str(int(s))
        cnt = 0

        while shortNum > 0:
            shortNum = int(shortNum / 10)
            cnt += 1
    
        for i in range(11 - cnt):
            midString = str(int(0)) + midString
        
        return midString 
            
