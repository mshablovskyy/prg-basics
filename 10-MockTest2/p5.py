# (p5.py) Define a function f(first_letter,last_letter) that, 
# for the data.txt file, returns the number of words that start 
# with the first_letter and end with the last_letter. Example:
# f("w","d")  compare your result with other students

# \W(a\w*b)\W
import os
import re

path = os.path.dirname(__file__) + '/'

def f(first_l, last_l, FILE=path + "Files/data.txt"):
    with open(FILE) as file:
        text = file.read()
    l = re.findall(f"\W({first_l}\w*{last_l})\W", text)
    return len(l)

print(f("w", "d"))

# , FILE=path + "Files/file.txt"