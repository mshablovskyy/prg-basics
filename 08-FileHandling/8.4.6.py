import os

path = os.path.dirname(__file__) + "/"
user_file = input("Enter file name: ")

try:
    with open(path + user_file) as file:
        text = file.read()
except FileNotFoundError:
    print("File not found!")
    exit()

lines = 0
for line in text.splitlines():
    lines += 1
    
words = 0
for word in text.split():
    words +=1
    
chars = 0
for char in text:
    chars += 1
        
print("lines:", lines)
print("words:", words)
print("chars:", chars)
        