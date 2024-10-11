price = float(input("Enter the price: "))
discount = float(input("Enter discount(%): "))

new_price = price - (price / 100 * discount)

print(f"New price = {round(new_price, 2)}")
print(f"Reduction = {round(price - new_price, 2)}")