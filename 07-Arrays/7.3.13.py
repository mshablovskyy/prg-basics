def in_arr(arr, item):
    for i in arr:
        if i == item:
            return True
    return False

arr = [15, 38, 7, 23, 14]
print(in_arr(arr, 2))