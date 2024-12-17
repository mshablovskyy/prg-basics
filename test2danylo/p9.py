def f(arr):
    for  i in range(len(arr)):
        if i ==0:
            if arr[i]!=arr[i+1]:
                if arr[i]!=arr[i+2]:
                    return arr[i]
                else:
                    return arr[i+1]
        elif i==len(arr)-1:
            if arr[i]!=arr[i-1]:
                if arr[i]!=arr[i-2]:
                    return arr[i]
                else:
                    return arr[i-1]
        if i !=0 and  i != len(arr)-1:
            if arr[i]!=arr[i+1]:
                if arr[i]!=arr[i-1]:
                    return arr[i]
if __name__=='__main__':
    print(f([25,25,23]))
    print(f([7,7,7,7,7,7,7,7,5]))