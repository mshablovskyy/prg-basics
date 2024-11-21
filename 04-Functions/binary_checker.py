def binary_number(var):
    result = True
    for i in var:
        if not(i == "0" or i == "1") and result:
            result = False
    return result