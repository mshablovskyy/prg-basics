def check(var):
    if var == "y":
        return True
    elif var == "n":
        return False
    
def ret(var):
    if var:
        return "Yes"
    elif not var:
        return "No"

print("SURVEY")

q1 = input("Are you interested in computer science? (y/n): ")
q2 = input("Do you like playing computer games? (y/n): ")
q3 = input("Do you have an Instagram account? (y/n): ")

print("SURVEY RESULTS")
print(f"Interested in computer science: {ret(check(q1))}")
print(f"Playing computer games: {ret(check(q2))}")
print(f"Has an Instagram account: {ret(check(q3))}")