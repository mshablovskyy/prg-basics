num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter the operator (+ or - or * or /): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    result = False

if result:
    print(f"{num1} {operator} {num2} = {result}")
else:
    print("Incorrect operator")