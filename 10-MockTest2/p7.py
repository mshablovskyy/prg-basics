import re
def f(arr):
    matches = []
    for i in arr:
        matches.append(bool(re.search("^(([a-z]|[0-9]|_){4,12})$", i)))
    x = 0
    for i in range(len(arr)):
        ok = True
        if ok and not matches[i]:
            ok = False
        if ok and not (bool(re.search("[a-z]", arr[i])) and bool(re.search("[0-9]", arr[i])) and bool(re.search("_", arr[i]))):
            ok = False
        if ok:
            x+=1
        
    return x
        
print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f", "hey_hey4gf444"]) )
# help(re)