import math
h = float(input('Enter your height in m: '))
d = round(3.57 * math.sqrt(h), 2)
print("The distance of the horison in km is: " + str(d))