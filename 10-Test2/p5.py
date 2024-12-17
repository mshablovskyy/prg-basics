def f(cart, prices, wallet):
    value = 0
    for k, v in cart.items():
        value += prices[k] * v
    if wallet >= value:
        return True
    else:
        return False
    
if __name__ == "__main__":
    cart = {"juice": 3, "bread": 1, "milk" : 2}
    prices = {"juice": 1.19, "bread": 1.99, "milk" : 1.49, "butter": 2.09}
    print(f(cart, prices, 10))
    print(f(cart, prices, 8))