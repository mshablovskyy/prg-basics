def f(computer, phone):
    return len(set(computer) | set(phone))

if __name__ == "__main__":
    computer = {"John", "Peter"}
    phone = {"Peter", "Frank", "Ann"}
    print(f(computer, phone))
    phone = {"Breeze", "Hunter", "Walker", "Chaser", "Camper", "Owl"}
    computer = {"Breeze", "Owl", "Storm", "Walker"}
    print(f(computer, phone))