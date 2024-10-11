number = input("Put your phone number: ")
x = 0
result = ""
for n in number:
    x += 1
    result += n
    if x == 3:
        result += "-"
        x=0
print(result)