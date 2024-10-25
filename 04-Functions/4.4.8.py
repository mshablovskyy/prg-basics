def time_check(time):
    if len(str(time)) == 1:
        return "0" + str(time)
    else:
        return time

def time_string(hour, minute, format):
    if format == "24":
        return str(time_check(hour)) + ":" + str(time_check(minute))
    elif format == "12":
        if hour == 0:
            return "12:" + str(time_check(minute)) + " AM"
        elif hour == 12:
            return "12:" + str(time_check(minute)) + " PM"
        elif hour < 12:
            return str(time_check(hour)) + ":" + str(time_check(minute)) + " AM"
        elif hour > 12:
            return str(time_check(hour - 12)) + ":" + str(time_check(minute)) + " PM"
        
print(time_string(1, 4, "12"))
        