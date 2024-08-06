from datetime import datetime
from datetime import date
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
from tkinter.messagebox import askokcancel
from tkinter import filedialog
from tkinter import *
from tkinter import END
from tkinter import ttk
from zipfile import ZipFile
from blacklist import BlackListApp
from AssignPending import AssignPendingApp

import pandas
import tkinter as tk
import os
import csv
import re
import ctypes

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tablet Finder")
        self.geometry("800x420")
        self.resizable(False, False)
        
        self.style = ttk.Style()
        self.style.configure("TLabel", font=("ROBOTO", 13, "bold"))
        self.style.configure("TButton", font=("ROBOTO", 13, "bold"))

          # Save the rendered SVG as a PNG file
        self.iconphoto(True, tk.PhotoImage(file="./icon/header-logo.png"))
        myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

        self.strSearchVar = tk.StringVar()
        self.editSearch = ttk.Entry(self, textvariable=self.strSearchVar, font=("ROBOTO", 13), width=74)
        self.editSearch.place(x=30, y=10)
        self.editSearch.bind("<Return>", (lambda event: self.dataSearch()))

        self.labelSearchClear = ttk.Label(self, background='white', text='r', font=("Webdings", 10, "bold"))
        self.labelSearchClear.place(x=702, y=11)
        self.labelSearchClear.bind("<Button-1>", (lambda event: self.LabelSearchClear()))

        self.labelUpdateStamp = ttk.Label(self, text="", font=("ROBOTO", 10, "italic"))
        self.labelUpdateStamp.place(x=600, y=38)

        self.labelOutput1 = ttk.Label(self, text="First name", font=("ROBOTO", 13, "bold"))
        self.labelOutput1.place(x=60, y=60)
        self.labelFirstName = ttk.Label(self, text="", font=("ROBOTO", 11))
        self.labelFirstName.place(x=75, y=88)
        self.labelCopy1 = tk.Label(self, text="2", font=("Wingdings 2", 18, "bold"))
        self.labelCopy1.bind("<Button-1>", (lambda event: self.LabelOutputCopy(1)))
        self.labelCopy1.place(x=47, y=88)

        self.labelOutput2 = ttk.Label(self, text="Last name", font=("ROBOTO", 13, "bold"))
        self.labelOutput2.place(x=60, y=120)
        self.labelLastName = ttk.Label(self, text="", font=("ROBOTO", 11))
        self.labelLastName.place(x=75, y=148)
        self.labelCopy2 = tk.Label(self, text="2", font=("Wingdings 2", 18, "bold"))
        self.labelCopy2.bind("<Button-1>", (lambda event: self.LabelOutputCopy(2)))
        self.labelCopy2.place(x=47, y=148)

        self.labelOutput3 = ttk.Label(self, text="Inmate ID", font=("ROBOTO", 13, "bold"))
        self.labelOutput3.place(x=60, y=180)
        self.labelInmateID = ttk.Label(self, text="", font=("ROBOTO", 11))
        self.labelInmateID.place(x=75, y=208)
        self.labelCopy3 = tk.Label(self, text="2", font=("Wingdings 2", 18, "bold"))
        self.labelCopy3.bind("<Button-1>", (lambda event: self.LabelOutputCopy(3)))
        self.labelCopy3.place(x=47, y=208)

        self.labelOutput4 = ttk.Label(self, text="Inmate Location", font=("ROBOTO", 13, "bold"))
        self.labelOutput4.place(x=60, y=240)
        self.labelInmateLocation = ttk.Label(self, text="", font=("ROBOTO", 11))
        self.labelInmateLocation.place(x=75, y=268)
        
        self.labelOutput5 = ttk.Label(self, text="Tablet ID", font=("ROBOTO", 13, "bold"))
        self.labelOutput5.place(x=420, y=60)
        self.labelTabletID = ttk.Label(self, text="", font=("ROBOTO", 11))
        self.labelTabletID.place(x=435, y=88)
        self.labelCopy5 = tk.Label(self, text="2", font=("Wingdings 2", 18, "bold"))
        self.labelCopy5.bind("<Button-1>", (lambda event: self.LabelOutputCopy(5)))
        self.labelCopy5.place(x=407, y=88)

        self.labelOutput6 = ttk.Label(self, text="MAC", font=("ROBOTO", 13, "bold"))
        self.labelOutput6.place(x=420, y=120)
        self.labelMac = ttk.Label(self, text="", font=("ROBOTO", 11))
        self.labelMac.place(x=435, y=148)
        self.labelCopy6 = tk.Label(self, text="2", font=("Wingdings 2", 18, "bold"))
        self.labelCopy6.bind("<Button-1>", (lambda event: self.LabelOutputCopy(6)))
        self.labelCopy6.place(x=407, y=148)

        self.labelOutput7 = ttk.Label(self, text="Tablet Location", font=("ROBOTO", 13, "bold"))
        self.labelOutput7.place(x=420, y=180)
        self.labelTabletLocation = ttk.Label(self, text="", font=("ROBOTO", 11))
        self.labelTabletLocation.place(x=435, y=208)

        self.labelOutput8 = ttk.Label(self, text="Last connection", font=("ROBOTO", 13, "bold"))
        self.labelOutput8.place(x=420, y=240)
        self.labelLastConnect = ttk.Label(self, text="", font=("ROBOTO", 11))
        self.labelLastConnect.place(x=435, y=268)

        self.labelOutput9 = ttk.Label(self, text="Tablet registration", font=("ROBOTO", 13, "bold"))
        self.labelOutput9.place(x=420, y=300)
        self.labelTabletRegistration = ttk.Label(self, text="", font=("ROBOTO", 11))
        self.labelTabletRegistration.place(x=435, y=328)
        
        self.buttonExport = ttk.Button(self, text="Print", command=self.exportOutputData)
        self.buttonExport.place(x=30, y=318)

        self.buttonExport = ttk.Button(self, text="Access", command=self.AccessToPIN)
        self.buttonExport.place(x=160, y=318)

        # Horizontal Lines
        self.line = ttk.Separator(self, orient=tk.HORIZONTAL)
        self.line.place(x=30, y=358, relwidth=0.93)

        self.line_Vertical = ttk.Separator(self, orient=tk.VERTICAL)
        self.line_Vertical.place(x=400, y=80, relheight=0.62)

        # self.buttonImport = ttk.Button(self, text="Import", command=self.showInputField)
        # self.buttonImport.place(x=60, y=370)

        # self.buttonReset = ttk.Button(self, text="Reset", command=self.StateReset)
        # self.buttonReset.place(x=30, y=370)

        self.buttonUploadZip = ttk.Button(self, text="Import", command=self.UploadFromZIP)
        self.buttonUploadZip.place(x=30, y=370)

        self.buttonViewBlacklist= ttk.Button(self, text="Blacklist", command=self.ViewBlacklist)
        self.buttonViewBlacklist.place(x=160, y=370)

        self.buttonAllList = ttk.Button(self, text="All List", command=self.ViewAllList)
        self.buttonAllList.place(x=290, y=370)

        self.buttonPendingList = ttk.Button(self, text="Export Pending", width=17, command=self.ExportPendingList)
        self.buttonPendingList.place(x=420, y=370)
        
        self.buttonAssignPending= ttk.Button(self, text="Assign Pending", width=17, command=self.AssignPendingList)
        self.buttonAssignPending.place(x=605, y=370)

        # DropDown ListBox
        self.dropDown = tk.Listbox(self, width=74, height=12, font=("ROBOTO", 13, "bold"),relief='flat', highlightbackground='SystemButtonFace')

        self.editSearch.bind('<Down>', self.PressDownKey)
        self.dropDown.bind('<Right>', self.PressReturnKey)
        self.dropDown.bind('<Return>', self.PressReturnKey)
        self.strSearchVar.trace('w', self.GetSearchData)

        self.dropDownStateFlag = False
        self.btnImportStateFlag = False

        self.readCSVFileData = []
        self.pendingList = []

        self.firstName = None
        self.lastName = None
        self.account = None
        self.PIN = None
        self.housingName = None
        self.serialNumber = None
        self.cdate = None
        self.MAC = None
        self.lastConnection = None
        self.fromRuckus = None
        self.Location = None

        self.dtypes_SCP = [
            'First Name',
            'Last Name',
            'Account #',
            'PIN'
        ]

        self.dtypes_InmateID = [
            'custodyAccount',
            'housingName'
        ]

        self.dtypes_Devices = [
            'serialNumber',
            'inmate.custodyAccount',
            'cdate'
        ]

        self.dtypes_ruckus = [
            'Hostname',
            'MAC',
            'AP Name',
            'Session start time'
        ]

        self.dtypes_Forti = [
            'device', 
            'mac'
        ]

        self.dtypes_Locations =[
            'From Ruckus',
            'Output'
        ]

        self.dtypes_blacklist = [
            'custodyAccount',
            'firstName',
            'lastName',
            'udate'
        ]

        self.dtypes_exclusion = [
            'First Name',
            'Last Name',
            'Account #',
            'unit'
        ]

        self.dtypes_TagReg = [
            'serialNumber',
            'Reg date'
        ]

        self.dtypes_sub = [
            'custodyAccount'
        ]

    def readData(self, file_path, colname):
        df = pandas.read_csv(file_path, usecols=colname)
        # print(df)
        return df

    def fileDialog(self, index):
        fileName = filedialog.askopenfilename()
        if fileName:
            self.readCSVFileData.append(self.readData(fileName, self.returnColName(index - 1)))

    def LabelClear(self):
        self.labelFirstName.configure(text="")
        self.labelLastName.configure(text="")
        self.labelInmateID.configure(text="", foreground="black")
        self.labelInmateLocation.configure(text="")
        self.labelTabletID.configure(text="")
        self.labelMac.configure(text="")
        self.labelTabletLocation.configure(text="")
        self.labelLastConnect.configure(text="")
        self.labelTabletRegistration.configure(text="")
    
    def GlobalVariableClear(self):
        self.firstName = None
        self.lastName = None
        self.account = None
        self.PIN = None
        self.customerID = None
        self.siteID = None
        self.housingName = None
        self.serialNumber = None
        self.cdate = None
        self.MAC = None
        self.lastConnection = None
        self.fromRuckus = None
        self.Location = None

    def AllStateReload(self):
        self.readCSVFileData.clear()
        self.pendingList.clear()
        self.editSearch.delete(0, "end")
        self.LabelClear()

    def StateReset(self):
        if askquestion(title="Information", message = "Do you initialize all data?") == "yes":
            self.AllStateReload()
        
    def dataSearch(self):
        if not self.readCSVFileData:
            showinfo(title="Warning", message = "Don't exist the data. Please check the CSV file")
        else:
            if len(self.readCSVFileData) >= 4:
                self.LabelClear()
                self.GlobalVariableClear()

                searchKeys = self.editSearch.get().split(", ")
                
                # self.firstName = self.GetDataFrameValue(self.readCSVFileData[0], )
                for oIdx, oRow in self.readCSVFileData[0].iterrows():
                    oRow = oRow.fillna(0)
                    if str(searchKeys[0]) == oRow[0] and str(searchKeys[1]) == oRow[1] and str(int(self.StringNumberMinus(searchKeys[2])) == str(int(oRow[2]))):
                        self.firstName = oRow[0]
                        self.lastName = oRow[1]
                        self.account = oRow[2]
                        self.PIN = oRow[3]
                        break
                
                self.housingName = self.GetDataFrameValue(self.readCSVFileData[1], 'custodyAccount', self.account, 'housingName')
                # for tIndex, tRow in self.readCSVFileData[1].iterrows():
                #     tRow = tRow.fillna(0)
                #     if str(int(tRow[0])) == self.account:
                #         self.housingName = str(tRow[1])
                #         break

                self.serialNumber = self.GetDataFrameValue(self.readCSVFileData[2], 'inmate.custodyAccount', self.account, 'serialNumber')
                # for thIndex, thRow in self.readCSVFileData[2].iterrows():
                #     thRow = thRow.fillna(0)
                #     if str(int(thRow[1])) == self.account:
                #         self.serialNumber = str(thRow[0])
                #         break
                
                self.mac = self.GetDataFrameValue(self.readCSVFileData[3], 'device', self.serialNumber, 'mac')
                # for foIndex, fourRow in self.readCSVFileData[3].iterrows():
                #     fourRow = fourRow.fillna(0)
                #     if str(fourRow[0]) == self.serialNumber:
                #         self.MAC = str(fourRow[1])
                #         break
                # print("============Start FromRuckus===========")
                # print(repr(self.MAC))

                self.lastConnection = self.GetDataFrameValue(self.readCSVFileData[4], 'MAC', str(self.mac).upper(), 'Session start time')
                self.fromRuckus = self.GetDataFrameValue(self.readCSVFileData[4], 'MAC', str(self.mac).upper(), 'AP Name')
                # for fiveIndex, fiveRow in self.readCSVFileData[4].iterrows():
                #     if str(fiveRow[1]) == str(self.MAC).upper():
                #         self.lastConnection = str(fiveRow[3])
                #         self.fromRuckus = str(fiveRow[2])
                #         break
                # print("============End FromRuckus===========")

                self.Location = self.GetDataFrameValue(self.readCSVFileData[5], 'From Ruckus', self.fromRuckus, 'Output')
                # for sixIndex, sixRow in self.readCSVFileData[5].iterrows():
                #     if str(sixRow[0]) == self.fromRuckus:
                #         self.Location = str(sixRow[1])
                #         break
                #     else:
                #         if self.fromRuckus == 0:
                #             self.Location = None
                
                self.cdate = self.GetDataFrameValue(self.readCSVFileData[8], 'serialNumber', self.serialNumber, 'Reg date')
                # for nine, nineRow in self.readCSVFileData[8].iterrows():
                #     nineRow = nineRow.fillna(0)
                #     if str(nineRow[0]) == self.serialNumber:
                #         self.cdate = str(nineRow[1])
                #         break

                self.subCust = self.GetDataFrameValue(self.readCSVFileData[9], 'custodyAccount', self.account, 'custodyAccount')
                
                self.labelFirstName.configure(text=str(self.firstName))
                self.labelLastName.configure(text=str(self.lastName))
                self.labelInmateID.configure(text=self.StringIDNumberMatch(self.account))
                self.labelInmateLocation.configure(text=str(self.housingName))
                self.labelTabletID.configure(text=str(self.serialNumber))
                self.labelMac.configure(text=str(self.MAC))
                self.labelTabletLocation.configure(text=str(self.Location))
                self.labelLastConnect.configure(text=str(self.lastConnection))
                self.labelTabletRegistration.configure(text=str(self.cdate))

                if not self.subCust == "":
                    self.labelInmateID.configure(foreground='red')

            else:
                showinfo(title="Warning", message = "Don't exist the data. Please check the CSV file")
    
    def PressReturnKey(self, pWidget):
        mWid = pWidget.widget

        index = int(mWid.curselection()[0])
        value = mWid.get(index)
        self.strSearchVar.set(value)
        self.dropDown.delete(0, END)
        
        self.dropDownStateFlag = False
        self.dropDown.place_forget()
        
        self.editSearch.focus()
        self.editSearch.icursor(tk.END)

        self.dataSearch()

    def PressDownKey(self, pWidget):
        self.dropDown.focus()
        self.dropDown.selection_set(0)

    def GetSearchData(self, *args):
        searchData = self.strSearchVar.get()
        self.dropDown.delete(0, END)

        if not bool(searchData):
            self.dropDown.place_forget()
            self.dropDownStateFlag = False 
        else:
            if self.dropDownStateFlag == False:
                self.dropDown.place(x=30, y=35)
                self.dropDownStateFlag = True
            # self.dropDown.delete(0, END)
            pattern = re.compile(searchData, re.IGNORECASE)

            patternData = []
            for frmIndex, frmElements in self.readCSVFileData[0].iterrows():
                if any(re.match(pattern, str(element)) for element in frmElements):
                    patternData.append(frmElements)

            for houseIndex, housing in self.readCSVFileData[1].iterrows():
                for frmE in patternData:
                    if str(int(housing[0])) == str(int(frmE[2])):
                        self.dropDown.insert(tk.END, str(frmE[0]) + ", " + str(frmE[1]) + ", " + str(self.StringIDNumberMatch(frmE[2])) + ", " + str(housing[1]))
                        break
                
    def exportOutputData(self):
        protossInmates = self.housingName.split("/")
        Unit = protossInmates[1]
        Cell = protossInmates[2]
        currentTime = str(date.today())
        exportSet = [self.firstName, self.lastName, self.StringIDNumberMatch(self.account), self.StringPINNumberMatch(self.PIN), Unit, Cell, currentTime]
        
        fields = ["FirstName", "LastName", "InmateID", "InmatePIN", "Unit", "Cell", "Date"]
        filename = "export_output.csv"

        with open(filename, 'w', newline='') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
        
            # writing the fields
            csvwriter.writerow(fields)
            # writing the data rows
            csvwriter.writerow(exportSet)
            # showinfo("Information", message="Export the searching data successfully in directory: ../export_output.csv")

    def ViewBlacklist(self):
        print(self.readCSVFileData[6])
        viewList = BlackListApp(self.readCSVFileData[6])
        viewList.mainloop()

    def ViewAllList(self):
        firstName = None
        lastName = None
        account = None
        pin = None
        housingName = None
        serialNumber = None
        cdate = None
        mac = None
        lastConnection = None
        fromRuckus = None
        Location = None

        fields = ["FirstName", "LastName", "InmateID", "InmatePIN", "Location", "AID", "MAC", "Tablet Location", "Last Connection", "Tablet Registration"]
        filename = "All List.csv"
        exclusUnit = []

        if not self.readCSVFileData:
            showinfo(title="Warning", message = "Don't exist the data. Please check the CSV file")
        else:
            if len(self.readCSVFileData) >= 4:
                with open(filename, 'w', newline='') as csvfile:
                    # creating a csv writer object
                    csvwriter = csv.writer(csvfile)
                    # writing the fields
                    csvwriter.writerow(fields)
                    for oIdx, oRow in self.readCSVFileData[0].iterrows():
                        oRow = oRow.fillna(0)
                        firstName = oRow[0]
                        lastName = oRow[1]
                        account = oRow[2]
                        pin = oRow[3]

                        housingName = self.GetDataFrameValue(self.readCSVFileData[1], 'custodyAccount', account, 'housingName')
                        # for tIndex, tRow in self.readCSVFileData[1].iterrows():
                        #     tRow = tRow.fillna(0)
                        #     if str(int(tRow[0])) == account:
                        #         housingName = str(tRow[1])
                        #         break
                    
                        serialNumber = self.GetDataFrameValue(self.readCSVFileData[2], 'inmate.custodyAccount', account, 'serialNumber')
                        # for thIndex, thRow in self.readCSVFileData[2].iterrows():
                        #     thRow = thRow.fillna(0)
                        #     if str(int(thRow[1])) == account:
                        #         serialNumber = str(thRow[0])
                        #         break
                        
                        mac = self.GetDataFrameValue(self.readCSVFileData[3], 'device', serialNumber, 'mac')
                        # for foIndex, fourRow in self.readCSVFileData[3].iterrows():
                        #     fourRow = fourRow.fillna(0)
                        #     if str(fourRow[0]) == serialNumber:
                        #         mac = str(fourRow[1])
                        #         break

                        lastConnection = self.GetDataFrameValue(self.readCSVFileData[4], 'MAC', str(mac).upper(), 'Session start time')
                        fromRuckus = self.GetDataFrameValue(self.readCSVFileData[4], 'MAC', str(mac).upper(), 'AP Name')
                        # for fiveIndex, fiveRow in self.readCSVFileData[4].iterrows():
                        #     if str(fiveRow[1]) == str(mac).upper():
                        #         lastConnection = str(fiveRow[3])
                        #         fromRuckus = str(fiveRow[2])
                        #         break

                        Location = self.GetDataFrameValue(self.readCSVFileData[5], 'From Ruckus', fromRuckus, 'Output')
                        # for sixIndex, sixRow in self.readCSVFileData[5].iterrows():
                        #     if str(sixRow[0]) == fromRuckus:
                        #         Location = str(sixRow[1])
                        #         break
                        #     else:
                        #         if fromRuckus == 0:
                        #             Location = None
                        
                        cdate = self.GetDataFrameValue(self.readCSVFileData[8], 'serialNumber', serialNumber, 'Reg date')
                        # for nine, nineRow in self.readCSVFileData[8].iterrows():
                        #     nineRow = nineRow.fillna(0)
                        #     if str(nineRow[0]) == serialNumber:
                        #         self.cdate = str(nineRow[1])
                        #         break
                        print([firstName, lastName, self.StringIDNumberMatch(account), self.StringPINNumberMatch(pin), str(housingName), str(serialNumber), str(mac), str(Location), str(lastConnection), str(cdate)])
                        csvwriter.writerow([firstName, lastName, self.StringIDNumberMatch(account), self.StringPINNumberMatch(pin), str(housingName), str(serialNumber), str(mac), str(Location), str(lastConnection), str(cdate)])
                        # exclusUnit.append([firstName, lastName, self.StringIDNumberMatch(account), self.StringPINNumberMatch(pin), str(housingName), str(serialNumber), str(mac), str(Location), str(lastConnection), str(cdate)])

                    # for index, element in enumerate(exclusUnit):
                                        
                
            else:
                showinfo(title="Warning", message = "Don't exist the data. Please check the CSV file")

    def ExportPendingList(self):     
        fields = ["FirstName", "LastName", "InmateID", "InmatePIN", "Unit", "Cell", "Date"]
        filename = "ExportPendingList.csv"
        exclusUnit = []
        with open(filename, 'w', newline='') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields
            csvwriter.writerow(fields)
            
            scpList = self.readCSVFileData[0].values.tolist()

            # print("\n===================Start scpList - 1====================")
            for i, element in self.readCSVFileData[2].iterrows():
                scpList = [sublist for sublist in scpList if element[1] not in sublist]
                # for sublist in scpList:
                #     if element[1] not in sublist:
                #         print(element[1], sublist)

            # print("\n===================End scpList - 1====================")
            for sub in scpList:
                for j ,inmateID in self.readCSVFileData[1].iterrows():
                    if sub[2] == inmateID[0] or str(inmateID[1]) == 'nan':
                        scpList.remove(sub)

            for sub1 in scpList:
                for k, blackElement in self.readCSVFileData[6].iterrows():
                    if sub1[2] == blackElement[0]:
                        scpList.remove(sub1)
                    # print(blackElement[1], blackElement[2], blackElement[2])
            
            print("\n===================Start scpList - 1====================")
            print(scpList)
            print("\n===================End scpList - 1====================")

            for i, sub2 in enumerate(scpList):
                for l, exclusElement in self.readCSVFileData[7].iterrows():
                    if sub2[2] == exclusElement[2]:
                        scpList.remove(sub2)
                    if i == 0:
                        exclusUnit.append(str(exclusElement[3]))
            
            for sub3 in scpList:
                if str(sub3[0]) == "nan" or str(sub3[1]) == "nan":
                    scpList.remove(sub3)

            scpList = [sublist for sublist in scpList if not isinstance(sublist[0], float)]

            print("\n===================Start Result===================")
            print(scpList)
            print("\n===================End Result=====================")

            # print("\n===================start match=====================")
            finalhousing = []
            tempScpList = []
            for finalPendElement in scpList:
                for idx, housing in self.readCSVFileData[1].iterrows():
                    if housing[0] == finalPendElement[2]:
                        # print(housing[0], finalPendElement[2])
                        tempScpList.append(finalPendElement)
                        finalhousing.append(housing[1])
                        break
            # print("\n===================End match=====================")

            print("\n===================Start FinalHousing===================")
            print(finalhousing)
            print("\n===================End FinalHousing=====================")
            print("\n===================Start exclusUnit===================")
            print(exclusUnit)
            print("\n===================End exclusUnit=====================")
            print("\n===================Start SCPLIST===================")
            print(scpList)
            print("\n===================End SCPLIST=====================")
            print("\n===================Start house===================")
            print(finalhousing)

            for m, unitElement in enumerate(exclusUnit):
                finalhousing_copy = finalhousing.copy()
                scpList_copy = tempScpList.copy()
                for finIndex, house in enumerate(finalhousing_copy):
                    unit = house.split("/")
                    # print(unit[1])
                    # print(unitElement[0], unitElement[1])
                    # print(unit[1], unitElement)
                    if unit[1] == unitElement:
                        print(unit[1])
                        tempScpList.remove(scpList_copy[finIndex])
                        finalhousing.remove(house)
            print(finalhousing)
            print("\n===================End house=====================")
            
            
            for index, ele in enumerate(tempScpList):
                protossInmates = finalhousing[index].split("/")
                Unit = protossInmates[1]
                Cell = protossInmates[2]
                currentTime = str(date.today())
                exportSet = [ele[0], ele[1], self.StringIDNumberMatch(ele[2]), self.StringPINNumberMatch(ele[3]), Unit, Cell, currentTime]
                self.pendingList.append(exportSet)
                # writing the data rows
                csvwriter.writerow(exportSet)

            showinfo("Information", message="Export the pending list successfully in directory: ../ExportPendingList.csv")
    
    def AssignPendingList(self):
        if not self.pendingList == []:
            assignApp = AssignPendingApp(self.pendingList)
            assignApp.mainloop()
        else:
            showinfo("Information", message="Can't find the pending list.")
    def UploadFromZIP(self):
        #All state Initialize
        # if askquestion(title="Information", message = "Do you initialize all data?") == "yes":
            self.AllStateReload()
            self.labelUpdateStamp.configure(text="")
            #Read the files to unzip from zip
            _path = filedialog.askopenfilename()
            if _path:
                directory, fileName = os.path.split(_path)
                
                with ZipFile(_path, 'r') as zObject: 
                    # Extracting all the members of the zip  
                    # into a specific location. 
                    file_names = zObject.namelist()
                    zObject.extractall(path=directory)
                print(file_names)
                if self.readCSVFileData == []:
                    if len(file_names) == 10:
                        for index, filename in enumerate(file_names):     
                            self.readCSVFileData.append(self.readData(directory  + "/" + filename, self.returnColName(index)))
                    else:
                        showinfo("Information", "Please the check the zip file")
                self.labelUpdateStamp.configure(text=str(datetime.now().strftime("%m/%d/%Y - %H:%M")))

    def AccessToPIN(self):
        self.clipboard_clear()
        self.clipboard_append(self.StringIDNumberMatch(self.account) + " " + self.StringPINNumberMatch(self.PIN))
        self.update()

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

    def StringNumberMinus(self, s):
        midString = str(s)
        while(midString.startswith('0')):
            midString = midString[1:]
        return midString
    
    def GetDataFrameValue(self, df, keyCol, keyVal, valCol):
        filterRow = df[df[keyCol] == keyVal]
        if not filterRow.empty:
            return str(filterRow.iloc[0][valCol])
        else:
            return ""

    def LabelOutputCopy(event, index):
        if index == 1:
            event.clipboard_clear()
            event.clipboard_append(event.labelFirstName.cget("text"))
            event.update() # now it stays on the clipboard after the window is closed
        elif index == 2:
            event.clipboard_clear()
            event.clipboard_append(event.labelLastName.cget("text"))
            event.update() # now it stays on the clipboard after the window is closed
        elif index == 3:
            event.clipboard_clear()
            event.clipboard_append(event.labelInmateID.cget("text"))
            event.update() # now it stays on the clipboard after the window is closed
        elif index == 5:
            event.clipboard_clear()
            event.clipboard_append(event.labelTabletID.cget("text"))
            event.update() # now it stays on the clipboard after the window is closed
        elif index == 6:
            event.clipboard_clear()
            event.clipboard_append(event.labelMac.cget("text"))
            event.update() # now it stays on the clipboard after the window is closed

    def returnColName(self, index):
        if index == 0:
            return self.dtypes_SCP
        elif index == 1:
            return self.dtypes_InmateID
        elif index == 2:
            return self.dtypes_Devices
        elif index == 3:
            return self.dtypes_Forti
        elif index == 4:
            return self.dtypes_ruckus
        elif index == 5:
            return self.dtypes_Locations
        elif index == 6:
            return self.dtypes_blacklist
        elif index == 7:
            return self.dtypes_exclusion
        elif index == 8:
            return self.dtypes_TagReg
        elif index == 9:
            return self.dtypes_sub
    
    def LabelSearchClear(event):
        print("success")
        event.editSearch.delete(0, END)

    def onClosing(self):
        if askokcancel("Quit", "Do you want to quit?"):
            self.destroy()
        else: 
            return
            

if __name__ == "__main__": 
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.onClosing)
    app.mainloop()




