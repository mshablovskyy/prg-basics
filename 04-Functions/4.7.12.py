def asterisk(n):
    result = ""
    for i in range(0, n - 1):
        result += "*/"
    result += "*"
    return result

print(asterisk(1))
print(asterisk(4))