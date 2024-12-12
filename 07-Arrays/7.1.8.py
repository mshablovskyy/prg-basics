computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

n = 0
while n < len(computer_games):
    print(str(n + 1) + ": " + computer_games[n])
    n += 1

print()

computer_games.sort()

n = 0
while n < len(computer_games):
    print(str(n + 1) + ": " + computer_games[n])
    n += 1