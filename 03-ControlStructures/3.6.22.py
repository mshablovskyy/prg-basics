text = ""

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        text += "Bingo" + " "
    elif i % 3 == 0:
        text += "Three" + " "
    elif i % 5 == 0:
        text += "Five" + " "
    else:
        text += str(i) + " "
        
print(text)