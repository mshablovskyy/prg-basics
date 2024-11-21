def pal(word):
    back = ""
    for i in word:
        back = i + back
    
    if word == back:
        return True
    else:
        return False
    
print(pal("raddar"))