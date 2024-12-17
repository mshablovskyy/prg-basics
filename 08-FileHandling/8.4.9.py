import csv
import os

path = os.path.dirname(__file__) + "/"

with open(path + "it_company.csv") as file:
    text = csv.reader(file)
    next(text)
    print("GRAPHIC DESIGNERS")
    print("=================")
    for line in text:
        if line[2] == "Graphic Designer":
            print(f"{line[1]} {line[0]}, {line[3]}")