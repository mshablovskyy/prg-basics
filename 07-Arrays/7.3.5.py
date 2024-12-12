arr = [15, 8, 31, 47, 2, 19]

res = 0

for i in arr:
    res += i
res = res / len(arr)  
  
print(res)

res = 0
i = 0
while i < len(arr):
    res += arr[i]
    i += 1
    
res = res / len(arr)  
  
print(res)