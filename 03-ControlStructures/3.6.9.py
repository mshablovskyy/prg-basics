name = input("Enter your name: ")

vowels = ["e", "i", "o", "u", "y"]

if name[-1] == "a":
    print(f"Your polish female name is {name}")
elif name[-1] in vowels:
    print(f"Your polish female name is {name[0: -1]}a")
else:
    print(f"Your polish female name is {name}a")
