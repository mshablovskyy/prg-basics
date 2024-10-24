# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

j_time = 40
u_time = 70
s_time = 20
r_time = 15
sp_time = 9

cor = True

if extra_rinse == "y":
    total_washing_time += r_time
if extra_spin == "y":
    total_washing_time += sp_time
if program == "j":
    total_washing_time += j_time
elif program == "u":
    total_washing_time += u_time
elif program == "s":
    total_washing_time += s_time
else:
    cor = False
    print("Incorrect input")
    
if cor:
    print(f"Washing time is {total_washing_time}")