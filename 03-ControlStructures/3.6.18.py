x = 2
y = 3

q = 0

if x > 0 and y > 0:
    q = 1
elif x < 0 and y > 0:
    q = 2
elif x < 0 and y < 0:
    q = 3
elif x > 0 and y < 0:
    q = 4
    
print(f"Point P({x},{y}) is in the {q} quadrant of the coordinate system")