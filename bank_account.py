class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder
        self.__balance = balance
        self.pin = pin
        self.transactions = []

    def deposit(self, amount):
        self.__balance += amount
        self.transactions.append(f"Deposited {amount}")
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.transactions.append(f"withdrawn {amount}")
            print(f"withdrawn: {amount}")
            print("Withdrawal successful")
        else:
            print("insufficient balance")

    def check_balance(self):
        print(f"Current balance: {self.__balance}")

    def show_transactions(self):
        print("Transaction History")
        for t in self.transactions:
            print(t)


accounts = {
    "Ramya": BankAccount("Ramya", 5000, 1234),
    "Renu": BankAccount("Renu", 8000, 4321)
}

name = input("Enter account holder name: ")
pin = int(input("Enter PIN: "))

if name in accounts and accounts[name].pin == pin:
    account = accounts[name]
    print("Login Successfull")
else:
    print("Invalid account or PIN")
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
