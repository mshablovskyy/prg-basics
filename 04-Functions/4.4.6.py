week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
def day_name(day_number):
    result = week[day_number - 1]
    return result

for i in range(1, 8):
    print(f'The name of day {i} in the week is {day_name(i)}')