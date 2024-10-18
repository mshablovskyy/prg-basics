###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    code = ord(char)
    code += 1
    encrypted_text += chr(code)

print(plain_text)
print(encrypted_text)