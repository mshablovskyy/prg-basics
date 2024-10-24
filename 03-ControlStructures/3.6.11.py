old_price = 200
current_price = 180

if old_price - old_price * 0.1 >= current_price:
    print(f"Old price = {old_price}")
    print(f"Current price = {current_price}")
    print(f"Price redused by {int((old_price - current_price) / old_price * 100)}%")
    print("Buy it!")