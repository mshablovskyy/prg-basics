arr = [2, 3, 2, 5, 8, 1, 9, 8]

def f(arr):
    new_arr = []
    for i in arr:
        times = -1
        for j in arr:
            if i == j:
                times += 1
        if not times:
            new_arr.append(i)
    return new_arr

print(f(arr))