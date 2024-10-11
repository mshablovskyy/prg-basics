import random
print("Dice rolling simulator")
result = ""
for i in range(5):
    dice_roll = random.randint(1,6)
    result += str(dice_roll) + " "
print(result)