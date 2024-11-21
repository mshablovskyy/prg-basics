def count(text, letter):
    text = text.lower()
    x = 0
    for l in text:
        if l == letter:
            x += 1
    return x