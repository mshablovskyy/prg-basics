def f(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    
if __name__ == "__main__":
    print(f(5,2))
    print(f(-5,2))
    print(f(-5,-3))
    print(f(5,-3))