def f(a, b):
    nums = range(a, b + 1)
    result = 0
    for i in nums:
        if len(str(i)) == 2:
            result += i
    return result

if __name__ == "__main__":
    l1 = [8, 98]
    l2 = [12, 104]
    for i in range(0, len(l1)):
        print(f(l1[i], l2[i]))