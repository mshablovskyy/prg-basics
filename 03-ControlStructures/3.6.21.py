am = int(input("Enter the amount in PLN: "))
amount = am

pln5 = am//5
am = am%5
pln2 = am//2
am = am%2
pln1 = am//1
am = am%1

print(f"{amount} PLN in coins, {pln5} - 5 PLN coins, {pln2} - 2 PLN coins, {pln1} - 1 PLN coins")