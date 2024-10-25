import math

def triangle_area(a,b,c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f'The area of ​​a triangle with sides 3, 4, 5 is {triangle_area(3, 4, 5)}')
print(f'The area of ​​a triangle with sides 5, 12, 13 is {triangle_area(5, 12, 13)}')
print(f'The area of ​​a triangle with sides 7, 24, 25 is {triangle_area(7, 24, 25)}')