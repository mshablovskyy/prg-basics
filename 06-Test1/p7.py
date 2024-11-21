def f(a, b):
    fib = [0,1]

    while fib[-1] <= b:
        fib.append(fib[-2] + fib[-1])
        
    result = 0
    for i in fib:
        if i >= a and i <=b:
            result += i
    return result

if __name__ == "__main__":
        print(f(1,5))
        print(f(6,21))
        print(f(30,90))