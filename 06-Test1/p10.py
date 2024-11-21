def f(time1, time2):
    TIME1 = time1
    TIME2 = time2

    if time1[-2:] == "am":
        time1 = time1[:-2]
    elif time1[-2:] == "pm":
        if time1[1] == ":":
            time1 = str(int(time1[0]) + 12) + time1[1:-2]
        else:
            time1 = str(int(time1[0:2]) + 12) + time1[2:-2]
    
    if time2[-2:] == "am":
        time2 = time2[:-2]
    elif time2[-2:] == "pm":
        if time2[1] == ":":
            time2 = str(int(time2[0]) + 12) + time2[1:-2]
        else:
            time2 = str(int(time2[0:2]) + 12) + time2[2:-2]

    if time1[1] == ":":
        hours1 = time1[0]
    else:
        hours1 = time1[0:2]

    if time2[1] == ":":
        hours2 = time2[0]
    else:
        hours2 = time2[0:2]

    if int(hours1) < int(hours2):
        return TIME1
    elif int(hours1) > int(hours2):
        return TIME2
    elif int(hours1) == int(hours2):
        if int(time1[-2:]) < int(time2[-2:]):
            return TIME1
        elif int(time1[-2:]) > int(time2[-2:]):
            return TIME2
        elif int(time1[-2:]) == int(time2[-2:]):
            return TIME1
        
    

if __name__ == "__main__":
    l = [["13:06", "13:12"], ["1:38pm", "13:31"], ["08:08", "8:01am"], ["6:00pm", "18:00"]]
    for i in l:
        print(f(i[0], i[1]))