time = int(input("How many hours have you been parked: "))
if time <= 0:
    print("No fee")
elif time <= 2:
    print("Fee is 5 PLN")
elif time <=6:
    print("Fee is 15 PLN")
else:
    print("Fee is 20 PLN")