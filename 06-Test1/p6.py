def f(st1, st2):
    grades1 = 0
    grades2 = 0
    for i in st1:
        if i == "3" or i == "4" or i == "5":
            grades1 += 1
    for i in st2:
        if i == "3" or i == "4" or i == "5":
            grades2 += 1
    
    if grades1 > grades2:
        return 1
    if grades1 < grades2:
        return 2
    if grades1 == grades2:
        return 0
    
if __name__ == "__main__":
    l1 = ["3,4,5", "3,2,5", "3,2,5,2,2"]
    l2 = ["4,3", "5,5,2,5", "4,4"]
    for i in range(0, len(l1)):
        print(f(l1[i], l2[i]))