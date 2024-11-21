def f(text):
    result = ""
    for i in text:
        result += i + "-"
    return result[:-1]

print(f("Univesity"))
print(f("x"))
print(f("UE"))
print(f(""))
