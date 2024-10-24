age = int(input("Enter dog's age: "))

if age <= 2:
    dog_age = age * 10.5
else:
    dog_age = 21 + (age - 2) * 4
    
print(f"Dogs age in dogs years is {dog_age}")