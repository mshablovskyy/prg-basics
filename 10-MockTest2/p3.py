def f(array2):
    dim = len(array2)
    for i in range(dim):
        row = 0
        col = 0
        for x in range(dim):
            row += array2[i][x]
            col += array2[x][i]
        if row != col:
            return False
    return True

# print(f([[3,7,2],
#          [4,2,5],
#          [5,2,1]]) )
# print(f([[3,7,2],
#          [7,2,5],
#          [2,5,1]]) )
print(f([
    [5, 1, 2, 6],
    [1, 6, 5, 2],
    [2, 5, 6, 1],
    [6, 2, 1, 5]
]))