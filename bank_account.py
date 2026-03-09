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
            self.transactions.append(f"Withdrawn {amount}")
            print(f"Withdrawn: {amount}")
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current balance: {self.__balance}")

    def show_transactions(self):
        print("Transaction History")
        for t in self.transactions:
            print(t)
