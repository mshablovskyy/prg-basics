def f(text):
    
    if len(text) < 6:
        return False
    
    for i in text:
        times = -1
        for j in text:
            if i == j:
                times += 1
        if times:
            return False
    return True

print(f('123dd6'))