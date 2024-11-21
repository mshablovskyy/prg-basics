def f(card_number):
    return card_number[:2] + "*" * (len(card_number) - 6) + card_number[-4:]

if __name__ == "__main__":
    print(f("2020141420201515"))
    print(len(f("2020141420201515")))