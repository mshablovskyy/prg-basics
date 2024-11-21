def f(num):
    l = []
    n = 1
    while len(l) < num:
        n += 1
        prime = True
        for i in range(2, n):
            if prime and n % i == 0:
                prime = False
        if prime:
            l.append(n)
    return l

print(f(1))
print(f(5))