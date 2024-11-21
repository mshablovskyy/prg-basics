def f(n1,n2,n3):
    l = [n1, n2, n3]
    result = True
    for i in l:
        t = -1
        for j in l:
            if i == j:
                t += 1
        if t:
            result = False
    return result

if __name__ == "__main__":
    print(f(4,8,5))
    print(f(2,9,2))
