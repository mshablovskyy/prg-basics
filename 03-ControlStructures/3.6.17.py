t24 = input("Enter 24-hour format time (--:--): ")
if len(t24) == 5:
    if t24[0:2] == "00":
        t12 = "12" + t24[2:] + "AM"
    elif t24[0:2] == "12":
        t12 = "12" + t24[2:] + "PM"
    elif int(t24[0:2]) < 12:
        t12 = t24 + "AM"
    elif int(t24[0:2]) > 12:
        t12 = str(int(t24[0:2]) - 12) + t24[2:] + "PM"
    print(t12)
else:
    print("Incorrect input")
    
