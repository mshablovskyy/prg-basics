# def f(arr):
#     if arr[0] == arr[1] and arr[1] == arr[2]:
#         key = arr[0]
#         for i in arr:
#             if i != key:
#                 return i
#     else:
#         arr = arr[:3]
#         x = arr[0]
#         x1 = []
#         x2 = []
#         for i in arr:
#             if i == x:
#                 x1.append(i)
#             else:
#                 x2.append(i)
#         if len(x1) < len(x2):
#             return x1[0]
#         else: return x2[0]
            
def f(arr):
    for i in range(2,len(arr)):
        if arr[i-2] != arr[i-1]:
            if arr[i-1] != arr[i]:
                return arr[i-1]
            elif arr[i-2] != arr[i]:
                return arr[i-2]
    return arr[-1]
    
if __name__ == "__main__":
    print(f([5, 7, 7, 7, 7, 7, 7, 7]))
    print(f([7, 5, 7, 7, 7, 7, 7, 7]))
    print(f([7, 7, 5, 7, 7, 7, 7, 7]))
    print(f([7, 7, 7, 5, 7, 7, 7, 7]))
    print(f([7, 7, 7, 7, 5, 7, 7, 7]))
    print(f([7, 7, 7, 7, 7, 5, 7, 7]))
    print(f([7, 7, 7, 7, 7, 7, 5, 7]))
    print(f([7, 7, 7, 7, 7, 7, 7, 5]))