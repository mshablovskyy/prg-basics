def f(var):
    people = 0
    for i in var:
        if i == "+":
            people += 1
        elif i == "-":
            people -= 1
        if people == 3:
            return True
    return False

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))