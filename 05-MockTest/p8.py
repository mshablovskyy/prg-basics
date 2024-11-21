def f(text):
    text_b = ""
    for i in text:
        text_b = i + text_b
    if text == text_b:
        return True
    else:
        return False

if __name__ == "__main__":
    print(f("radar"))