with open("08-FileHandling/pets.txt") as file:
    text = file.read()

print(text)
words = 0

lines = text.splitlines()
for line in lines:
    for i in line.split():
        words += 1
        
print(words)