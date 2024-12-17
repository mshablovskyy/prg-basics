def f(c):
    k=['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    for i in k:
        if i in c:
            continue
        else:
            return str(i)
if __name__=="__main__":
    print(f('2345678TJQKA'))
    print(f('2K345AQJ967T'))