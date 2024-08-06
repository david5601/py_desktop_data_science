import csv
import pandas

# Function to read CSV file and return a set of values from a specific column
def read_column_values(file_path, column_name):
    values = set()
    # print(column_name)
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        column_names = reader.fieldnames
        for row in reader:
            # print(row)
            # if column_name in column_names:
            values.add(row[column_name])
    return values

# Function to write data to a CSV file
def write_to_csv(file_path, data, columns):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)

def GetDataFrameValue(df, keyCol, keyVal, valCol):
    filterRow = df[df[keyCol] == keyVal]
    if not filterRow.empty:
        print(str(filterRow.iloc[0][valCol]))
        return str(filterRow.iloc[0][valCol])
    else:
        return ""
    
def StringPINNumberMatch(s):
    shortNum = int(s)
    midString = str(int(s))
    cnt = 0

    while shortNum > 0:
        shortNum = int(shortNum / 10)
        cnt += 1
    
    for i in range(7 - cnt):
        midString = str(int(0)) + midString
        
    return midString

def StringNumberMinus(s):
    midString = str(s)
    while(midString.startswith('0')):
        midString = midString[1:]
    return midString

# Read Protoss.csv
with open('./Protoss.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    protos_columnNames = reader.fieldnames

with open('./cr68TabletReportbyunit.csv', mode='r', newline='') as file:
    reader = csv.DictReader(file)
    cr68_columnNames = reader.fieldnames

protoss_df = pandas.read_csv("./Protoss.csv", usecols=['serialNumber', protos_columnNames[4]])
cr68_df = pandas.read_csv("./cr68TabletReportbyunit.csv", usecols=cr68_columnNames)

# FILE #1 - NewTablets.csv
new_tablets_data = []
tablet_replacement_data = []
for index, protoss in protoss_df.iterrows():
    if GetDataFrameValue(cr68_df, cr68_columnNames[0], protoss[1], cr68_columnNames[1]) == "":
        new_tablets_data.append([StringPINNumberMatch(protoss[1]), protoss[0]])
        
    if GetDataFrameValue(cr68_df, cr68_columnNames[1], protoss[0], cr68_columnNames[0]) == "":
        tablet_replacement_data.append([StringPINNumberMatch(protoss[1]), protoss[0]])

write_to_csv('NewTablets.csv', new_tablets_data, ['InmateID', 'AID'])
write_to_csv('Tablet_Replacement.csv', tablet_replacement_data, ['InmateID', 'AID'])

# FILE #3 - Discrepancies.csv
discrepancies_data = []
for index, cr68 in cr68_df.iterrows():
    if GetDataFrameValue(protoss_df, protos_columnNames[4], cr68[0], 'serialNumber') == "":
        discrepancies_data.append([StringPINNumberMatch(cr68[0]), cr68[1]])
write_to_csv('Discrepancies.csv', discrepancies_data, ['InmateID', 'AID'])

print("CSV processing completed successfully.")
