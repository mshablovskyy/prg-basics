# (p5.py) Define a function f(first_letter,last_letter) that, 
# for the data.txt file, returns the number of words that start 
# with the first_letter and end with the last_letter. Example:
# f("w","d")  compare your result with other students
import os
path = os.path.dirname(__file__) + '/'
punc_m = [".", ",", "-", "'", '"', "(", ")", '[', ']']

def f(first_l, last_l, FILE=path + "Files/data.txt"):
    with open(FILE) as file:
        text = file.read()
        text = text.split()
    r = 0
    for word in text:
        for i in range(len(word)//2):
            if word[0] in punc_m:
                word = word[1:]
            if word[-1] in punc_m:
                word = word[:-1]
            
        if word[0] == first_l and word[-1] == last_l:
            r += 1
    return r

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
l = []
for i in letters:
    for j in letters:
        l.append(f(i, j))
print(l)