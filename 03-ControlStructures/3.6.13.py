###
# Checking whether a car exceeded the speed limit
#
speed_limit_min = 40
speed_limit_max = 140
car_speed = int( input('Enter car speed (km/h): ') )

if car_speed > speed_limit_max or car_speed < speed_limit_min:
    print(f'Your speed is {car_speed}km/h')
    print('Warning: invalid speed!!')
else:
    print("Speed is OK")
    