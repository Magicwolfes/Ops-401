#Sierra Maldonado
#!/usr/bin/env python3
from openpyxl import Workbook
import datetime


workbook = Workbook()
sheet = workbook.active
# Define column names

column_names = ['Company', 'Job Name', 'Job Url Link', 'Applied Date', 'Comments', 'Today']

# Write column names to the first row
sheet.append(column_names)

def new():
    while True:
        Company = input("Company Name: ")
        Name = input("Job Name: ")
        Url = input("Job Url Link: ")
        Applied = input("Applied date: ")
        Comments = input("Comments: ")
        Today = datetime.datetime.now().date()
        sheet.append([Company, Name, Url, Applied, Comments, Today])
        workbook.save('JobHunting.xlsx')
        choose = input("Continue or exit? ")
        if choose == 'exit':
            break
        
def update():
    while True:
        row_number = int(input("Enter the row number to update or 0 to exit: "))
        if row_number == 0:
            break
        column_number = int(input("Enter the column to update: (5 For new Comments) "))
        new_data = input("Enter new data: ")
        sheet.cell(row=row_number, column=column_number).value = new_data
        workbook.save('JobHunting.xlsx')


while True:
    choose = input("New, update, or exit? ")
    if choose == "new":
        new()
    if choose == "update":
        update()
    if choose == "exit":
        break
        

