import os
def f(f):
    with open(f, "w") as file:
        for i in range(1, 101):
            file.write(f"{i}, {i**2}, {i**3}\n")

f(os.path.dirname(__file__) + "/numbers.txt")