tup = (50,20,40,50,30,50)

def count(tup, n):
    res = 0
    for i in tup:
        if i == n:
            res += 1
    return res

print(count(tup, 50))