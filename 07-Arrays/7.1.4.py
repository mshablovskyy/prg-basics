arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[len(arr)-2])
print('Sum of the first and last value', arr[0] + arr[-1])
print('middle value', arr[int(len(arr) / 2)])
res = ""
for i in arr:
    res += str(i) + " "
print('all array values separated by a single space', res)