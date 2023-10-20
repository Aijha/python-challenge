#First import os module and csv file
import os
import csv

#File to write
output_path = os.path.join('..', 'Resources', '/Users/aijhasymone/Desktop/ClassFolder/Python_HW/python-challenge/PyBank/Resources/budget_data copy.csv')

#Open the file to bregin writing and specifiy variables
with open(output_path, 'w') as csvfile:
    #initial writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    #Write 1st row (cloumn headers)
    csvwriter.writerow(['Date', 'Profit Losses'])

#Unsure of out_list importance but it is here for now!!
out_list = ['Date','Profit Losses'],['Profit Losses','Date']


