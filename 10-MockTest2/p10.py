def f(arr2):
    arr = []
    for row in arr2:
        for i in row:
            arr.append(i)
    sm = min(arr)
    for r in range(len(arr2)):
        for c in range(len(arr2[r])):
            if sm == arr2[r][c]:
                if r == c:
                    return True
                else:
                    return False
 
print(f([[7,8],[5,3],[9,4]]))  # 3, row 1, col 1
print(f([[7,8,5,3],[9,4,2,6]]))
