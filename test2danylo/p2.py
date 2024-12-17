def f(number):
    a=[0,1]
    for i in range(number*number):
        a.append(a[-1]+a[-2])
    if number in a:
        return True
    else:
        return False
if __name__=='__main__':
    print(f(1597))
