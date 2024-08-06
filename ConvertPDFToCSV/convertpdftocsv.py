# Import Module 
import tabula 
from pypdf import PdfReader
import pandas as pd
import itertools
# Read PDF File 
# this contain a list

msa = 'MSA #'
tablet_info = 'Tablet Info #'
msaList = []
tabletList = []

reader = PdfReader("cr68TabletReportbyunit.pdf")
print(f"The PDF document has {len(reader.pages)} pages in total")

for index in range(1, len(reader.pages)):
    # print(f"===================Start - {index}====================")
    df = tabula.read_pdf("cr68TabletReportbyunit.pdf", pages = index)[0]
    column_name = df.columns.tolist()
    msaList.append(df[column_name[2]].tolist())
    tabletList.append(df[column_name[3]].tolist())
    # readPDFfile.append([df[column_name[2]].tolist(), df[column_name[3]].tolist()])
    print([df[column_name[2]].tolist(), df[column_name[3]].tolist()])
    print("\n")

msaList = list(itertools.chain.from_iterable(msaList))
tabletList = list(itertools.chain.from_iterable(tabletList))

readPDFfile = pd.DataFrame({'MSA #': msaList,
                            'Tablet Info #': tabletList})
readPDFfile.to_csv("./ConvertProtossDevice.csv")
print(readPDFfile)
    # print(column_name)
    # df.to_csv('./cnv.csv')
    # print([df[column_name[2]].tolist(), df[column_name[3]].tolist()])
    # print(f"===================End - {index}======================")
# for index in range(len(readPDFfile[0])):
#     msaList.append([readPDFfile[0][index], readPDFfile[1][index]])
# print(msaList)
# Convert into Excel File 

