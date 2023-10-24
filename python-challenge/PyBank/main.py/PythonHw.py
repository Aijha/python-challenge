#First import os module and csv file
import os
import csv

#File to read and write
input_csvpath = os.path.join('..', 'Resources', '/Users/aijhasymone/Desktop/ClassFolder/Python_HW/python-challenge/PyBank/Resources/budget_data.csv')
output_csvpath = os.path.join('..', 'Resources', '/Users/aijhasymone/Desktop/ClassFolder/Python_HW/python-challenge/PyBank/Resources/output.txt')

with open(input_csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print("CSV Header: {csv_header}")

    month_count = 0
    sum_over_time = 0
    
    

    # Read each row of data after the header
    for row in csvreader:
        print(row)
        month_count = month_count+1
        sum_over_time = sum_over_time +int(row[1])
        

        

        

    print(month_count)
    print(sum_over_time)


#Open the file to bregin writing and specifiy variables
with open(output_csvpath, 'w') as csvfile:
    #initial writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    #Write 1st row (cloumn headers)
    csvwriter.writerow(['Date', 'Profit Losses'])
   
    

#Output Text File
out_list = ['Date','Profit Losses'],['Profit Losses','Date']



