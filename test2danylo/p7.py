def  f(array2D):
    p=0
    l=0
    for i in array2D:

            p+=i[0]
            l+=i[1]
    
    return p-l
if __name__=='__main__':
    print(f([[3,0]]))
    print(f([[3,0],[6,1]]))
