def evaluate_rpn_expression(tokens):
    stack = []
    for token in tokens:
        if token == "=":
            if len(stack) == 1:
                return stack.pop()
            else:
                raise ValueError("Invalid RPN expression.")
        elif token in ("+", "-", "*", "/"):
            if len(stack) < 2:
                raise ValueError("Not enough values in the stack for the operation.")
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                stack.append(a / b)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Invalid token: {token}")

# Example usage:
expressions = [
    "2 3 + =",
    "2 4 1 + * =",
    "2 3 + 4 5 + * =",
    "8 3 1 + / 3 2 - 4 + * ="
]

for expr in expressions:
    tokens = expr.split()
    try:
        result = evaluate_rpn_expression(tokens)
        print(f"Expression: {expr} -> Result: {result}")
    except Exception as e:
        print(f"Expression: {expr} -> Error: {e}")