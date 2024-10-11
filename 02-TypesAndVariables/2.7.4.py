import math
circumference = float(input("Enter tree circumference in cm: "))
permission = 50 <= circumference / math.pi
print(f"Tree can be cut down: {permission}")