def f(arr, val = "max"):
    min_v = arr[0][0]
    min_pos = [0,0]
    max_v = arr[0][0]
    max_pos = [0,0]
    for r in range(len(arr)):
        for i in range(len(arr[r])):
            if min_v > arr[r][i]:
                min_v = arr[r][i]
                min_pos = [r, i]
            if max_v < arr[r][i]:
                max_v = arr[r][i]
                max_pos = [r, i]
    if val == "max":
        return max_pos
    elif val == "min":
        return min_pos



print(f(arr = [[-38, 19], [5,40],[-7,11],[209,16]]))