distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input("Enter fuel consumption(per 100 km): "))
total_fuel_consumption = distance * fuel_consumption / 100
total_cost = total_fuel_consumption * fuel_price
print(f"Total fuel consumption: {round(total_fuel_consumption, 2)}")
print(f"Total cost: {round(total_cost, 2)}")