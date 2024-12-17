def f(x,y):
    if x>0:
        if y>0:
            return 1
        else:
            return 4
    if x<0:
        if y>0:
            return 2
        else: 
            return 3
if __name__=='__main__':
    print(f(5,2))
    print(f(-5,2))
    print(f(5,-2))

        