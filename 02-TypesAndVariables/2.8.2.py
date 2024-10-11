temp = float(input("Enter temperature in C: "))
temp_f = temp * 9 / 5 + 32
temp_k = temp + 273.15

print(f"temp in C: {round(temp, 2)}, temp in F: {round(temp_f, 2)}, temp in K: {round(temp_k, 2)}")