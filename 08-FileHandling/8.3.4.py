###
# Calculates the total value of money spent
#
import re # module for regular expressions
import os
# file name with shopping report
path = os.path.dirname(__file__) + "/"
email_file = path + 'report.txt'

# read the content of email
with open(email_file) as file:
    email = file.read()

# regular expression pattern
# for amounts
pattern = '\d+'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
res = 0
for amount in amounts:
    res += int(amount)

# print result
print(res)