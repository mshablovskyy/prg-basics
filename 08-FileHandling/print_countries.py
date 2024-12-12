###
# Reads from file, line by line
#
with open('08-FileHandling/countries.txt', 'r') as file:
    n=1
    for line in file:
        print(n, line, end="")
        n+=1