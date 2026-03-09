from atm import login

account = login()

if account is None:
    exit()

while True:
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account.check_balance()

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        account.deposit(amount)
        print("Deposit successful")

    elif choice == 3:
        amount = int(input("Enter withdrawn amount: "))
        account.withdraw(amount)

    elif choice == 4:
        account.show_transactions()

    elif choice == 5:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
