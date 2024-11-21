def f(num, even):
    num = str(num)
    result = 0
    x = 1
    if even:
        x = 0
    for i in num:
        if int(i) % 2 == x:
            result += int(i)
    return result

if __name__ == "__main__":
    print(f(3124, True))
    print(f(3124, False))
    print(f(20576, False))
    print(f(20576, True))
    print(f(13115, True))