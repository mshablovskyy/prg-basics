def f(text):
    space = True
    result = ""
    for i in text:
        if space:
            result += i
            space = False
        if i == " ":
            space = True
    return result

print(f("Internet of Things"))
print(f("For Your Information"))
print(f("Python"))