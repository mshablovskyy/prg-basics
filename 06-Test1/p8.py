def f(h, m, s):
    if h == m / 60 and m == s / 60 and h == s / 3600:
        return True
    else:
        return False

if __name__ == "__main__":
    l = [[1,60,3600], [2,120,7200], [4,220,14400,], [3,180,10600]]
    for i in l:
        print(f(i[0], i[1], i[2]))