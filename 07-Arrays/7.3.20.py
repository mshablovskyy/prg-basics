


arr = [7,9,2,4,5,6]

print(arr)

even_arr = []
odd_arr = []

for i in arr:
    if i%2 == 0:
        even_arr.append(i)
    else:
        odd_arr.append(i)
        
arr = even_arr + odd_arr

print(arr)