def f(thing, rinse, spin):
    result = 0
    if thing == "J":
        result += 40
    elif thing == "U":
        result += 70
    elif thing =="S":
        result += 20
    else:
        return "Incorrect input"
    if rinse:
        result += 15
    if spin:
        result += 9
    return result

if __name__ == "__main__":
    print(f("U", False, True))
    print(f("J", True, True))
    print(f("S", False, False))