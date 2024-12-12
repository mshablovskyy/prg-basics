import os
path = os.path.dirname(__file__)
filename = (path + "/seven_wonders.txt")

seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Sort data alphabetically
seven_wonders.sort()

# Write data to the file
with open(filename, 'w') as file:
    for item in seven_wonders:
        file.write(item + "\n")