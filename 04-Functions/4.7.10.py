def f(n1, n2):
    result = 0
    for i in range(n1, n2):
        if i % 2 == 0 and i < 0:
            result += 1
    return result

print(f(-7, 8))
print(f(-1, 11))