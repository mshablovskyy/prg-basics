l = ""
n = 1
nums = 10
num = 0

while num < nums:
    n += 1
    prime = True
    for i in range(2, n):
        if prime and n % i == 0:
            prime = False
    if prime:
        l = l + str(n) + " "
        num += 1

print(l)