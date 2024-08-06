from tkinter import ttk
import tkinter as tk

class BlackListApp(tk.Tk):
    def __init__(self, dataList):
        super().__init__()

        self.title("BlackList")
        self.geometry("500x400")
        self.resizable(False, False)

        # self.style = ttk.Style()
        # self.style.configure("TLabel", font=("ROBOTO", 20, "bold"))

        self.blackListView = ttk.Treeview(self, height=16)
        self.blackListView["columns"] = ["#1","#2","#3","#4"]

        self.blackListView.heading("#0", text="#")
        self.blackListView.heading("#1", text="Last Name")
        self.blackListView.heading("#2", text="First Name")
        self.blackListView.heading("#3", text="Inmate ID")
        self.blackListView.heading("#4", text="Banned Date")

        self.blackListView.column("#0", width=50)
        self.blackListView.column("#1", width=105)
        self.blackListView.column("#2", width=95)
        self.blackListView.column("#3", width=80)
        self.blackListView.column("#4", width=146)

        self.data = dataList

        for index, sublist in self.data.iterrows():
                sublist = sublist.fillna("-")
                print(sublist[0], sublist[1], sublist[2], sublist[3])
                if isinstance(sublist[3], str):
                    self.blackListView.insert("", "end",text=f"{int(index + 1)}", values=(f"{str(sublist[2])}", f"{str(sublist[1])}", f"{self.StringNumberMatch(sublist[0])}", f"{str(sublist[3])}"))
                elif isinstance(sublist[3], float):
                    self.blackListView.insert("", "end",text=f"{int(index + 1)}", values=(f"{str(sublist[2])}", f"{str(sublist[1])}", f"{self.StringNumberMatch(sublist[0])}", f"{str(sublist[3])}"))
        self.blackListView.pack(fill="both", expand=True)
        self.blackListView.place(x=10, y=40)

    def StringNumberMatch(self, s):
        shortNum = int(s)
        midString = str(int(s))
        cnt = 0

        while shortNum > 0:
            shortNum = int(shortNum / 10)
            cnt += 1
    
        for i in range(7 - cnt):
            midString = str(int(0)) + midString
        
        return midString      
# data = [["s","s","s","s","s"],["s","s","s","s","s"]]
# app = BlackListApp(data)
# app.mainloop()