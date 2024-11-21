def sum_even(var, even):
    x = 0
    result = 0
    if not even:
        x = 1
    for i in str(var):
        if int(i) % 2 == x:
            result += int(i)
    return(result)

print(sum_even(13115, True))