def ope(n1, n2, operator):
    return eval(f"{n1} {operator} {n2}")

print(ope(2,3, "+"))
print(ope(2,3, "%"))
print(ope(2,3, "**"))
print(ope(2,3, "*"))
print(ope(2,3, "-"))