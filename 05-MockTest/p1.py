def f(amount, coins = [5, 2, 1]):
    result = 0
    for i in coins:
        result += amount // i
        amount = amount % i
    return result

if __name__ == "__main__":
    print(f(23))
    print(f(8))
    print(f(21, [10, 5, 2, 1]))