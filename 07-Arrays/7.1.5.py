arr = []
for i in range(1,6):
    arr.append(i)
print(arr)
arr[0] = arr[0] - 1
print(arr)
arr[-1] = arr[-1] + 4
print(arr)
arr[len(arr)//2] = arr[len(arr)//2] * 2
print(arr)