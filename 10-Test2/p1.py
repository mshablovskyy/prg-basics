def f(expression):
    operators = ["*", "%"]
    expression = expression.split()

    n_operators = 0
    for i in expression:
        if i in operators:
            n_operators += 1

    for i in range(n_operators):
        num1 = 0
        num2 = 0
        for x in range(len(expression)):
            if expression[x] in operators:
                num1 = expression[x-2]
                num2 = expression[x-1]
                op = expression[x]
                expression[x] = eval(f"{num1} {op} {num2}")
                expression.pop(x-1)
                expression.pop(x-2)
                break
    return expression[0]


if __name__ == "__main__":
    print(f("5 4 *"))
    print(f("2 6 % 4 5 * *"))
    print(f("11 7 % 15 * 14 % "))