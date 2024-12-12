price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for k,v in price_list.items():
    print(f"{k}: {v}")
x = 0
for i in price_list.values():
    x += i
    
print(round(x,2))

for k in price_list:
    price_list[k] = price_list[k] * 0.9
print()
for k,v in price_list.items():
    print(f"{k}: {round(v, 2)}")
    
x = 0
for i in price_list.values():
    x += i
    
print(round(x,2))