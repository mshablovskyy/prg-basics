def f(n):
    result = ""
    for i in range(0, n):
        result += "*/"
    return result[:-1]

if __name__ == "__main__":
    l = [4, 1, 0, 6]
    for i in l:
        print(f(i))