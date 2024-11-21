def f(number):
    result = True
    for i in number:
        if not(i == "0" or i == "1") and result:
            result = False
    return result

if __name__ == "__main__":
    print(f("01010101010101010000010111101010"))
    print(f("0310w101010101010100000v10111101010"))