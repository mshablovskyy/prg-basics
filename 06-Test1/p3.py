def f(passw):
    if len(passw) < 6:
        return False
    for i in passw:
        times = -1
        for j in passw:
            if i == j:
                times += 1
        if times:
            return False
    return True

if __name__ == "__main__":
    l = ["ax15", "book123", "A2water3", "qwerty", ""]
    for i in l:
        print(f(i))