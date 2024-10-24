age = int(input('Enter your age: '))
if age < 13:
    print('You are child')
elif age < 20:
    print("You are teen")
elif age < 65:
    print("You are adult")
else:
    print("You are senior")