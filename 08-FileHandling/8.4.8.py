import re
import os

path = os.path.dirname(__file__) + "/"

filename = path + "files.txt"

with open(filename) as file:
    text = file.read()

l = re.findall(".+\..{4}", text)

for i in l:
    print(i)