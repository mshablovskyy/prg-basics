import os
import csv

path = os.path.dirname(__file__) + "/"

with open(path + "clothing.csv") as file:
    data = csv.reader(file)
    next(data)
    for line in data:
        if float(line[5]) < 60 and int(line[6]) < 40:
            print(line)
            