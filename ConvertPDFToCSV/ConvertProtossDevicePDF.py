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
    msaList = []
    tabletList = []
    msaTmp = []
    url = entry_pdf.get()
    reader = PdfReader(url)
    print(f"The PDF document has {len(reader.pages)} pages in total")

    for index in range(1, len(reader.pages)):
        df = tabula.read_pdf(url, pages = index)[0]
        column_name = df.columns.tolist()
        msaList.append(df[column_name[2]].tolist())
        tabletList.append(df[column_name[3]].tolist())
        # print([df[column_name[2]].tolist(), df[column_name[3]].tolist()])
        # print("\n")

    msaList = list(itertools.chain.from_iterable(msaList))
    tabletList = list(itertools.chain.from_iterable(tabletList))

    msaList = [str(element)[3:] for element in msaList]

    fields = ["MSA #", "Tablet Info #"]
    filename = "cr68TabletReportbyunit.csv"
    with open(filename, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for idx, element in enumerate(msaList):
            if not element == "":
                csvwriter.writerow([str(msaList[idx]), tabletList[idx]])

    # readPDFfile = pd.DataFrame({'MSA #': msaList,
    #                             'Tablet Info #': tabletList})
    # readPDFfile.to_csv("./ConvertProtossDevice.csv")
    # print(readPDFfile)

# Create GUI
root = tk.Tk()
root.title("PDF Table to CSV Converter")

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


