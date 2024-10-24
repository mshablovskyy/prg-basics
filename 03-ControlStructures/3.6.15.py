ean = input("Enter EAN-13 article number: ")
if len(ean) == 13 and ean.isdigit():
    print("EAN is correct")
else:
    print("EAN is incorrect")
if ean[0:3] == "590":
    print("It was manufactured in Poland")
else:
    print("It was not manufactured in Poland")