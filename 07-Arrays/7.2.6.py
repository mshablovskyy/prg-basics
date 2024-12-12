arr = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for row in arr:
    for item in row:
        print(item, end=" ")
    print()

for i in range(3):
    arr[i][i] = 1

print()

for row in arr:
    for item in row:
        print(item, end=" ")
    print()