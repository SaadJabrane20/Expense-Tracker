import tracker
def main():
    while True:

        tracker.display_menu()
        try:
            n = int(input("enter your choice : "))
        except ValueError:
            print("Invalid Choice! Enter a valid choice . ")
            continue
        if n < 0 or n > 7:
            print("invalid Choice, enter an option between 0 and 7: ")
            continue
        match n:
            case 1:
                try:
                    amount = float(input("Enter income amount: "))
                except ValueError:
                    print("Invalid valid, enter again: ")
                    continue
                category = input("Enter income Category : ")
                tracker.add_income(amount,category)
            case 2:
                amount = int(input("Enter expense amount: "))
                category = input("Enter expense category : ")
                tracker.add_expense(amount, category)
            case 0:
                print("exiting.......")
                break
if __name__ == "__main__":
    main()