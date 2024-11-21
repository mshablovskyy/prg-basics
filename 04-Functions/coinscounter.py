def coinscounter(amount, coins = [5, 2, 1]):
    result = 0
    amount = int(amount)
    for c in coins:
        result += amount // c
        amount = amount % c
    return result

print(coinscounter(23))