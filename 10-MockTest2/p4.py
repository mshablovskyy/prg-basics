def f(d):
    h_k = ""
    h_v = 0
    for k,v in d.items():
        x = 0
        for i in v:
            x += i
        x = x/len(v)
        if h_v < x:
            h_k = k
            h_v = x
    return h_k

print(f({"math":[5,4,4],"geo":[5,4,4,4],"comp":[5,4,4]}))