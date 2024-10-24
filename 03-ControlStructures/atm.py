###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

def check_pin():
    entered_pin = input("Enter your current pin: ")
    if entered_pin == pin:
        return True
    else:
        return False

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Change the pin")
    print("5. Exit")


    choice = input("Choose an option (1-4): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance and check_pin():
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance or incorrect pin.")
    elif choice == "4":
        print("Your are changing your pin. If you want to cancel it, type \"q\"")
        new = input("Enter your new pin or \"q\": ")
        if new != "q" and check_pin():
            if new.isdigit() and len(new) == 4:
                pin = new
                print(f"Your pin has changed. New pin is \"{pin}\"")
            else:
                print("Pin must contain only digits and be 4 symbols long. Operation was cancelled.")
        elif new == "q":
            print("Cancelled")
        else:
            print("You entered current pin incorrectly. Operation cancelled.")
    elif choice == '5':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
