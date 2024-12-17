def f(l):
    for i in range(2, len(l)):
        if l[i-2] != l[i-1]:
            if l[i-1] != l[i]:
                return l[i-1]
            elif l[i-2] != l[i]:
                return l[i-2]
    return l[-1]


if __name__ == "__main__":
    print(f([25,23,23]))
    print(f([7,7,7,7,7,5,7]))