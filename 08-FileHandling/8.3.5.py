###
# Checks the correctness of username and password
#
# username is at least 6 characters long
# username contains only lowercase letters
# password is at least 8 characters long
# password contains only letters (lowercase and uppercase), numbers, and the underscore character
import re

# read username and password from keyboard
username = input("username: ")
password = input("password: ")

# pattern (criteria) for username and password
username_pattern = "^[a-z]{6}[a-z]*$"
password_pattern = "^[a-zA-Z0-9_]{8}[a-zA-Z0-9_]*$"

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if username_match and password_match:
   print("Everything is Ok")
else:
   print("Bad username or password")