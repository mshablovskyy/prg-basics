###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    r = 0
    for n in str(abs(number)):
        r += int(n)
    return r

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')