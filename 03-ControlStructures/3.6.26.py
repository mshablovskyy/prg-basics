pin = "0805"
tries = 3

def check(var):
    global tries
    if var == pin:
        return True
    elif var != pin:
        tries -=1
        return False

while tries:
    if tries and check(input("Enter the PIN code: ")):
        print("Pin is correct")
        break
    else:
        print("Pin is incorrect")
        
if not tries:
    print("Sorry, your payment card has been blocked.")




