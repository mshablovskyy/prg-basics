def f(code):
    s = 0
    for i in code[:-1]:
        s += int(i)
    if s % 7 == int(code[-1]):
        return True
    else:
        return False
    
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))