# Final Project
# Banking App
# Class based
# Withdrawal and Deposit
# Write the transaction to a file
# While True, input, classes, open, methods, properties
from datetime import datetime


def write_account_file(file_name="banking.csv", content="/n"):
    with open(file_name, 'a') as file:
        file.write(content)


def read_account_balance(file_name="banking.csv", account_name=""):
    balance = 0.0
    with open(file_name, 'r') as file:
        for line in file:
            data = line.split(";")
            if account_name == data[0]:
                balance = float(data[1])
    return balance


class BankAccount:
    name = "empty"
    balance = 0.00

    def __init__(self, name):
        self.name = name

    def withdrawal(self, summa):
        result = self.balance
        result -= summa
        if result < 0.0:
            print("Operation can't be proceed. Not enough money on account")
        else:
            self.balance = result

    def deposit(self, summa):
        self.balance += summa


while True:
    account = input("Hi, pleas enter your account name:")
    bankAccount = BankAccount(account)
    BankAccount.balance = read_account_balance(account_name=account)
    print("Hi, " + BankAccount(account).name + ". You balance = " + str(BankAccount.balance))
    operation = input("Pleas select operation (w - withdrawal) or (d - deposit), (q - quit)")
    if operation == "w":
        amount = float(input("What amount do you want withdrawal?"))
        bankAccount.withdrawal(amount)
    elif operation == "d":
        amount = float(input("What amount do you want deposit?"))
        bankAccount.deposit(amount)
    elif operation == "q":
        print("Thank for use our service")
        break
    else:
        print("You select unknown operation, pleas repeat.")
        continue

    now = datetime.now().time()  # time object
    content_str = '' + bankAccount.name + ';' \
                  '' + str(bankAccount.balance) + ';' \
                  '' + operation + ';' \
                  '' + str(amount) + ';' \
                  '' + str(now) + ';' \
                  '\n'
    write_account_file(content=content_str)
