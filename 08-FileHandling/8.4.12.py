import os
import csv
path = os.path.dirname(__file__) + "/"
# The file books.csv contains a list of books. 
# Write a program that copies the book data from a given genre to 
# its corresponding file. Use functions to divide the 
# program into logical parts.

# Genre --> Filename
# Fantasy --> books_fantasy.txt
# Historical --> books_historical.txt
# Romance --> books_romance.txt
# Classic --> books_classic.txt 

def main(path = path, file = "books.csv"):
    with open(path + file) as f:
        data = csv.reader(f)
        for i in data:
            headers = i
            break
        next(data)
        content = []
        for i in data:
            content.append(i)
    
    genres = ["Fantasy", "Historical", "Romance", "Classic"]
    for genre in genres:
        text = sep_genre(genre, content)
        write(f"{path}books_{genre.lower()}.txt", text)
        

def sep_genre(genre, text):
    res = []
    for i in text:
        if i[2] == genre:
            res.append(i)
    return res

def write(filename, text):
    with open(filename, "w") as f:
        for i in text:
            t = ""
            for j in i:
                t += j + ", "
            f.write(t[:-2] + "\n")
        
    
    
main()
    