###
# Functions to read any data type from the keyboard
#
def input_string(message):
    return str(input(message))

def input_integer(message):
    return int(input(message))

def input_real(message):
    return float(input(message))

def input_boolean(message, tr, fl):
    mes = input(message)
    if mes == tr:
        return True
    elif mes == fl:
        return False