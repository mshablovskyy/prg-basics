num = int(input("Enter your number: "))

while not num == 1:
    num -= 1
    if num == 5:
        print("five")
    elif num == 4:
        print("four")
    elif num == 3:
        print("three")
    elif num == 2:
        print("two")
    elif num == 1:
        print("one")
    else:
        print(num)