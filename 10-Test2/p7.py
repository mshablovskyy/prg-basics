def f(arr2):
    people = 0
    for row in arr2:
        people += row[0]
        people -= row[1]
    return people

if __name__ == "__main__":
    print(f([[3,0]]))
    print(f([[3,0],[6,1]]))