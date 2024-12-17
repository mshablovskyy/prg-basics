def f(number):
    if number in create_fib(number):
        return True
    else:
        return False

def create_fib(border):
    fib = [0, 1]
    while fib[-1] < border:
        fib.append(fib[-2] + fib[-1])
    return fib

if __name__ == "__main__":
    print(f(5))
    print(f(4))
    print(f(13))
    print(f(150000))