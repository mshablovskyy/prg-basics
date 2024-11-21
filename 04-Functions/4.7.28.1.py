def f(dice):
    max_digit = dice[0]
    max_number = 1
    current_number = 1
    
    for i in range(0, len(dice)):
        if dice[i] == dice[i - 1]:
            current_number += 1
        else:
            if current_number > max_number:
                max_number = current_number
                max_digit = dice[i - 1]
            current_number = 1
    if current_number > max_number:
        max_digit = dice[i - 1]
    
    return max_digit

print(f("5233165554211"))
print(f("2133"))