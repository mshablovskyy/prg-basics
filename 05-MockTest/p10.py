def f(sentence):
    s = 0
    for i in sentence:
        s += ord(i)
    if s % 3 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f("hello world"))
    print(f("university"))
    print(f("student"))