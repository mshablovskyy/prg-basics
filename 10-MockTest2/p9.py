import os
import csv
path = os.path.dirname(__file__) + "/"

def f(value):
    with open(path + "Files/data.csv") as file:
        csv_data = csv.reader(file)
        next(csv_data)
        x = 0
        for row in csv_data:
            if int(row[9]) >= value:
                x+=1
        return x
            
print(f(9200))