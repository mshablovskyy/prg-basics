num = int(input("Enter the number of products purchased: "))
price = float(input("Enter the price of products purchased: "))
to_pay = 0

if num <= 2:
    to_pay += price * num
else:
    to_pay += price * 2
    to_pay += (price * 0.75) * (num - 2)
    
print(f"You have bought {num} products for {price} each")
print(f"With all discounts, you have to pay {to_pay}")