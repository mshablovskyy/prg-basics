def f(arr2):
    arr1 = []
    for r in arr2:
        for i in r:
            arr1.append(i)
    return arr1


array1 = [
    [2, 3],
    [1, 5]
]

array2 = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]

array3 = [
    [2, 1],
    [3, 5],
    [7, 4],
    [2, 6]
]

arrays = [array1, array2, array3]

for arr in arrays:
    print(f(arr))