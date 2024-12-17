
def f(addr):
    import re
    pat='^\w{1,2}[1-9999]+$'
    c=re.match(pat, addr)
    if c==None:
        return False
    else:
        return True
if __name__=='__main__':

    print(f('A4'))
    print(f('a4'))
    print(f('4a'))
    print(f('bC234'))
    print(f('g80'))
