###
# A program that prints your height both in cm and in feet and inches.
#
cm = 196
inches_raw = cm / 2.54
feet = int(inches_raw / 12)
inches = round(inches_raw % 12, 2)
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')