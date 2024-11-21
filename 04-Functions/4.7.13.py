def sum_n(n):
    result = ""
    for i in range(1, n + 1):
        result += str(i)
    return result
        
print(sum_n(4))
print(sum_n(11))