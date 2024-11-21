def f(text):
    c = True
    result = ""
    for i in text:
        if c:
            result += i
            c = False
        if i == " ":
            c = True
    return result

if __name__ == "__main__":
    print(f("Int of Thi"))
    print(f("For Your Info"))
    print(f("Python"))