paragraph = "cat dog mouse cat rat cat mouse"

paragraph = paragraph.split()
words = set(paragraph)

for word in words:
    c = 0
    for p in paragraph:
        if word == p:
            c+=1
    print(word, c)