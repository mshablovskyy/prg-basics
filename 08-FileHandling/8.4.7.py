import re

text = input("Enter text: ")
pattern = "a|e|y|u|i|o"
vowels = re.findall(pattern, text)
res = 0
for i in vowels:
    res += 1
    
print(f"Number of vowels: {res}")