import random
# COMPUTER TURN
computer = random.randint(1,6)
# YOUR TURN
you = int(input("Enter random number, 1 to 6: "))

print(f'You won: {computer == you}')
print(f'The number was {computer}')