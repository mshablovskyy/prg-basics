import rangecchecker

x = 6
lower = 5
higher = 10

if __name__ == "__main__":
    v = rangecchecker.check_range(x,lower,higher)
    if v:
        print(f"{x} is in range ({lower}, {higher})")
    else:
        print(f"{x} is not in range ({lower}, {higher})")