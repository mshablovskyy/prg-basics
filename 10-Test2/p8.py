def f(cards):
    Cards = ["A", "K", "Q", "J", "T", "9", "8","7", "6", "5","4", "3", "2"]
    cards_l = []
    for c in cards:
        cards_l.append(c)
    for i in set(Cards) - set(cards_l):
        return str(i)

if __name__ == "__main__":
    print(f("2345678TJQKA"))
    print(f("2K345AQJ967T"))