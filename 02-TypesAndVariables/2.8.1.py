import math
r = float(input("Enter radius: "))
area = r ** 2 * math.pi
circumference = r * 2 * math.pi

print(f"Radius: {round(r, 2)}, area: {round(area, 2)}, circumference: {round(circumference, 2)}")