def BubbleSort(arr):
    for j in arr:
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                x = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = x
    return arr

arr = [3,9,1,7,4,2,8,5,0,6,-4,-23,-67]

print(BubbleSort(arr))