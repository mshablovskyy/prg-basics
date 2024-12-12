import os
path = os.path.dirname(__file__) + "/"

file_name = path + "it_company.csv"

with open(file_name) as file:
    n = -1
    for line in file:
        if n == 5:
            input("Press \"Enter\" to continue")
            n = 0
        print(line[:-1])
        n += 1