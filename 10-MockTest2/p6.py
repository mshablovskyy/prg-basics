import os
import json
path = os.path.dirname(__file__) + "/"

def f(years, course, average_grade, file=path + "Files/data.json"):
    with open(file) as f:
        students = json.load(f)
    num = 0
    for i in students:
        avg = 0
        for j in i["studies"]["courses"]:
            if j["name"] == course:
                g = 0
                for n in j["grades"]:
                    g+=n
                avg = g / len(j["grades"])
        if i["age"] >= years and avg >= average_grade:
            num +=1
    return num
    
print(f(21, "statistics", 4))