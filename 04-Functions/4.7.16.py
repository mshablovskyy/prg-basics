def fib(num):
    n1 = 0
    n2 = 1
    for i in range(0, num - 1):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    return n1

print(fib(6))