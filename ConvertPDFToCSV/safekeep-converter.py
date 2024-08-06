import PyPDF2
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import csv

def extract_table(pdf_file_path):
    text = ""
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for index, page_num in enumerate(reader.pages):
            # print(page_num)
            page = reader.pages[index]
            text += page.extract_text()
    print(text)
    return text

def convert_to_csv(pdf_file_path, csv_file_path):
    text = extract_table(pdf_file_path)
    # print(text)
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        for line in text.split('\n'):
            csvwriter.writerow(line.split('\t'))

def browse_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        entry_pdf.delete(0, tk.END)
        entry_pdf.insert(0, file_path)

def convert_pdf_to_csv():
    pdf_file_path = entry_pdf.get()
    if pdf_file_path:
        csv_file_path = pdf_file_path.rsplit('.', 1)[0] + ".csv"
        convert_to_csv(pdf_file_path, csv_file_path)
        messagebox.showinfo("Conversion Complete", "PDF table successfully converted to CSV!")

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
