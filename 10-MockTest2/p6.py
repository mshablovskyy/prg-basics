import os
path = os.path.dirname(__file__) + "/"

def f(years, course, average_grade, file=path + "Files/data.json"):
    with open(file) as f:
        text = f.read()
    text = text.splitlines()
    print(text)
    
print(f(21, "statistics", 4))