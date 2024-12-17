def f(computer,smartphone):
    d={
    }
    c=0
    for i in computer:
        d[i]=0
    for i in smartphone:
        d[i]=0
    for i in d:
        c+=1
    return c
if __name__=='__main__':
    print(f(computer={'John','Peter'}, smartphone={'Peter','Frank','Ann'} ))
    print(f(computer={'Breeze','Hunter','Walker','Chaser','Camper','Owl'}, smartphone={'Breeze','Owl','Storm','Walker'}))