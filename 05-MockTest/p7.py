def f(n):
    n1 = 0
    n2 = 1
    for i in range(n - 1):
        res = n1 + n2
        n1 = n2
        n2 = res
    return n1

if __name__ == "__main__":
    print(f(5))
    print(f(9))