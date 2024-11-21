import monthgetter

def main():
    m = input("Enter number of your month: ")
    month = monthgetter.get_month(m)
    print(f"Your month {m} is {month}")
    
if __name__ == "__main__":
    main()

