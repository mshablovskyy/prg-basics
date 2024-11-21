def f(expression):
    nums = []
    opers = []
    
    for i in range(0,len(expression)):
        if i % 2 == 0:
            nums.append(expression[i])
        else:
            opers.append(expression[i])
    
    result = int(nums[0])
    nums = nums[1:]
    
    for i in range(0, len(nums)):
        if opers[i] == "+":
            result += int(nums[i])
        elif opers[i] == "-":
            result -= int(nums[i])
            
    return result
    
print(f("2+3-4+5-0"))