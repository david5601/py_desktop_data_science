import csv

# Function to read CSV file and return a set of values from a specific column
def read_column_values(file_path, column_name):
    values = set()
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            values.add(row[column_name])
    return values

# Function to write data to a CSV file
def write_to_csv(file_path, data, columns):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)

# Read Protoss.csv
protoss_custody_accounts = read_column_values('./Protoss.csv', 'inmate.custodyAccount')
protoss_serial_numbers = read_column_values('./Protoss.csv', 'serialNumber')
# protoss_aids = read_column_values('Protoss.csv', 'AID')

# Read cr68TabletReportbyunit.csv
cr68_msa_numbers = read_column_values('./cr68TabletReportbyunit.csv', 'MSA #')
cr68_tablet_info_numbers = read_column_values('./cr68TabletReportbyunit.csv', 'Tablet Info #')
# cr68_aids = read_column_values('cr68TabletReportbyunit.csv', 'AID')
# cr68_inmate_ids = read_column_values('cr68TabletReportbyunit.csv', 'InmateID')

# FILE #1 - NewTablets.csv
new_tablets_data = []
tablet_replacement_data = []
for account, serialNmuber in zip(protoss_custody_accounts, protoss_serial_numbers):
    if account not in cr68_msa_numbers:
        new_tablets_data.append([account, serialNmuber])
    if serialNmuber not in cr68_tablet_info_numbers:
        tablet_replacement_data.append([account, serialNmuber])

write_to_csv('NewTablets.csv', new_tablets_data, ['InmateID', 'AID'])
write_to_csv('Tablet_Replacement.csv', tablet_replacement_data, ['InmateID', 'AID'])
# # FILE #2 - Tablet_Replacement.csv

# for serial_number, inmate_id, aid in zip(protoss_serial_numbers, cr68_inmate_ids, protoss_aids):
#     if serial_number not in cr68_tablet_info_numbers:
#         tablet_replacement_data.append([inmate_id, aid])
# write_to_csv('Tablet_Replacement.csv', tablet_replacement_data, ['InmateID', 'AID'])

# FILE #3 - Discrepancies.csv
discrepancies_data = []
for msa_number, tablet_info in zip(cr68_msa_numbers, cr68_tablet_info_numbers):
    if msa_number not in protoss_custody_accounts:
        discrepancies_data.append([msa_number, tablet_info])
write_to_csv('Discrepancies.csv', discrepancies_data, ['InmateID', 'AID'])

print("CSV processing completed successfully.")
