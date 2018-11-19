import csv
import os

def WriteDictToCSV(csv_file,csv_columns,dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError as err:
            print("I/O error")    
    return            

csv_columns = ['Row','Name','Country']
dict_data = [
    {'Row': 1, 'Name': 'Alex', 'Country': 'India'},
    {'Row': 2, 'Name': 'Ben', 'Country': 'USA'},
    {'Row': 3, 'Name': 'Shri Ram', 'Country': 'India'},
    {'Row': 4, 'Name': 'Smith', 'Country': 'USA'},
    {'Row': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
    ]

currentPath = os.getcwd()
csv_file = currentPath + "/Names.csv"

WriteDictToCSV(csv_file,csv_columns,dict_data)