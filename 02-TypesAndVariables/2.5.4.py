amount = float(input("Enter the amount: "))
vat = round(amount / 100 * 23, 2)
print(f"Amount: {amount}")
print(f"Vat 23%: {vat}")