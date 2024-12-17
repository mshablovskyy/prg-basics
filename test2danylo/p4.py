def f(subjects):
    f=0
    r=''
    min=1000000000000000000
    for k,v in subjects.items():
        c=0
        for i in v:
            c+=i
            f=c/len(v)
        if f<min:
            min=f
            r=k
    return r


if __name__=='__main__':


    print(f({'bio':[3,3,4,4,3],'his':[3,3,4,3,3]}))
    print(f({'math':[3,4,4],'geo':[5,4,4,4],'comp':[5,4]}))