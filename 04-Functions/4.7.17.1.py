def pal(word):
    result = True
    for i in range((len(word)//2)+1):
        if word[i] != word[-(i + 1)] and result:
            result = False
    return result
            
print(pal("raddar"))