import tabula 
from pypdf import PdfReader
import pandas as pd
import itertools
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import csv

def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        entry_pdf.delete(0, tk.END)
        entry_pdf.insert(0, file_path)

def convert_pdf_to_csv():
    nameList = []
    firstNameList = []
    lastNameList = []
    nameList = []
    msaList = []
    unitList = []

    nameTmp = []
    msaTmp = []
    unitTmp = []

    url = entry_pdf.get()
    reader = PdfReader(url)
    print(f"The PDF document has {len(reader.pages)} pages in total")
    # df = tabula.read_pdf(url, pages = 1)[0]
    # print(df)
    for index in range(0, len(reader.pages)):
        print(tabula.read_pdf(url, pages = 0))
        if not tabula.read_pdf(url, pages = 0) == []:
            df = tabula.read_pdf(url, pages = index)[0]
            column_name = df.columns.tolist()
            nameTmp.append(df[column_name[0]].tolist())
            msaTmp.append(df[column_name[1]].tolist())
            unitTmp.append(df[column_name[4]].tolist())
            # print([df[column_name[0]].tolist(), df[column_name[1]].tolist(), df[column_name[1]].tolist()])
            print("\n")

    nameTmp = list(itertools.chain.from_iterable(nameTmp))
    msaTmp = list(itertools.chain.from_iterable(msaTmp))
    unitTmp = list(itertools.chain.from_iterable(unitTmp))
    # print(len(nameList), len(msaList), len(unitTmp))
    # unitTmp = unitList
    for index, unitEle in enumerate(unitTmp):
        unit = str(unitEle).split("/")[0]
        unit = unit.replace(unit[:4], '')
        msaTmp[index] = str(msaTmp[index]).replace(msaTmp[index][:3], '')
        if unit != "120A Bed":
            unitList.append(unit)
            nameList.append(nameTmp[index])
            msaList.append(msaTmp[index])
            

    print(len(nameList), len(msaList), len(unitList))
    for index, element in enumerate(nameList):
        firstNameList.append(str(element).split(',')[0])
        lastNameList.append(str(element).split(',')[1])
    firstNameList.append("*")
    lastNameList.append("*")
    msaList.append("*")
    unitList.append("120A Bed")

    # readPDFfile = pd.DataFrame({'First Name': firstNameList,
    #                             'Last Name': lastNameList,
    #                             'Account #': msaList,
    #                             'unit': unitList})
    fields = ["First Name", "Last Name", "Account #", "unit"]
    filename = "ExclusionsConvert.csv"
    with open(filename, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for idx, element in enumerate(firstNameList):
            if msaList[idx] != "*":
                csvwriter.writerow([firstNameList[idx], lastNameList[idx], StringIDNumberMatch(msaList[idx]), unitList[idx]])
            else:
                csvwriter.writerow([firstNameList[idx], lastNameList[idx], msaList[idx], unitList[idx]])
    # readPDFfile.to_csv("./ExclusionsConvert.csv")
    # print(readPDFfile)
            
def StringIDNumberMatch(s):
    shortNum = int(s)
    midString = str(int(s))
    cnt = 0

    while shortNum > 0:
        shortNum = int(shortNum / 10)
        cnt += 1
    
    for i in range(7 - cnt):
        midString = str(int(0)) + midString
        
    return midString

# Create GUI
root = tk.Tk()
root.title("Exclusions Converter")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_pdf = tk.Label(frame, text="PDF File:")
label_pdf.grid(row=0, column=0)

entry_pdf = tk.Entry(frame, width=50)
entry_pdf.grid(row=0, column=1)

button_browse = tk.Button(frame, text="Browse", command=browse_pdf)
button_browse.grid(row=0, column=2)

button_convert = tk.Button(frame, text="Convert", command=convert_pdf_to_csv)
button_convert.grid(row=1, columnspan=3, pady=10)

root.mainloop()


