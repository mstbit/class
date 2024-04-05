# ##### read CSV files #####

# ### import 
import csv

with open('members_chen.csv', newline='') as csvfile:
    persons = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in persons:
        print(', '.join(row))
        
        
        