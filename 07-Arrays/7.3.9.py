# 1. ["water","book","sky"]   ["water","book","sky"]
# 1. [True,False]   [True,False,True]
# 1. [5,3,1]   [5,3,1]
# 1. [3,2,1]   [3,2]

def check(arr1, arr2):
    if arr1 == arr2:
        return True
    return False

print(check(["water", "book", "sky"], ["water", "book", "sky"]))
print(check([True, False], [True, False, True]))
print(check([5, 3, 1], [5, 3, 1]))
print(check([3, 2, 1], [3, 2]))