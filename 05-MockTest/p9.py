def f(text):
    vowels = ["a", "e", "i", "o", "u", "y"]
    result = 0
    for i in text:
        for v in vowels:
            if i == v:
                result += 1
    return result

if __name__ == "__main__":
    print(f("wata"))
    print(f("university"))
    print(f("aeiouybbbb"))