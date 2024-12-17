arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(5):
    arr[0][i] = i+1

for r in range(1,5):
    for c in range(5):
        arr[r][c] = arr[0][c] * (r + 1)


print(arr)