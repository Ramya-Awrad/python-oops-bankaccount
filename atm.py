from bank_account import BankAccount

accounts = {
    "Ramya": BankAccount("Ramya", 5000, 1234),
    "Renu": BankAccount("Renu", 8000, 4321)
}

def login():
    name = input("Enter account holder name: ")
    pin = int(input("Enter PIN: "))

    if name in accounts and accounts[name].pin == pin:
        print("Login Successful")
        return accounts[name]
    else:
        print("Invalid account or PIN")
        return None
