def f(sizes):
    numS = 0
    numM = 0
    numL = 0
    for i in sizes:
        if i == "S":
            numS += 1
        elif i == "M":
            numM += 1
        elif i == "L":
            numL += 1
    if numS <= numM and numS <= numL:
        return "S"
    elif numM <= numS and numM <= numL:
        return "M"
    elif numL <= numS and numL <= numM:
        return "L"
    
if __name__ == "__main__":
    l = ["L,S,L,M,L,S,S,L", "M,L,L,L,M", "M,L,M,L,S,S,S"]
    for i in l:
        print(f(i))