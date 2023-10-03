from BankApp.account import Account
from BankApp.bank import Bank


class ATMMachine:

    def __init__(self):
        self.Tranxactrust = ""
        self.userInput = 0
        self.firstName = ""
        self.lastName = ""
        self.pin = 0
        self.userAccount = ""
        self.balance = 0
        self.account = ""
        self.bank = Bank("Tranxactrust")
        self.bank1 = Account("Account number", "User", "pin")

    def main(self):
        self.main_menu()

    def main_menu(self):
        self.userInput = int(input(
            """Welcome to Tranxactrust!
            Press:
            1 -> Open new account
            2 -> Deposit
            3 -> Withdraw
            4 -> Transfer
            5 -> Check balance
            """))

        if self.userInput == 1:
            self.open_account()
        elif self.userInput == 2:
            self.deposit()
        elif self.userInput == 3:
            self.withdraw()
        elif self.userInput == 4:
            self.transfer()
        elif self.userInput == 5:
            self.check_balance()

    def check_balance(self):
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        balance = self.bank.get_balance(account_number, pin)
        print(f"Balance: {balance}")

    def transfer(self):
        target_account_number = input("Enter target account number: ")
        amount = int(input("Enter amount to transfer: "))
        pin = input("Enter PIN: ")

        self.bank.transfer(amount, "1", target_account_number, pin,)

    def withdraw(self):
        account_number = input("Enter account number: ")
        pin = input("Enter PIN: ")
        amount = int(input("Enter amount to withdraw: "))

        self.bank.withdraw(amount, account_number, pin)
        self.bank1.withdraw(amount, account_number)
        balance = self.balance - amount

        print(f"Account balance for {account_number} is ${balance}")
        self.main_menu()
        # self.bank.deposit(deposit_amount, account_number)
        # self.bank1.transfer(amount)

    def deposit(self):
        account_number = input("Enter account number: ")
        # pin = input("Enter PIN: ")
        deposit_amount = float(input("Enter amount to deposit: "))

        self.bank.deposit(deposit_amount, account_number)
        self.bank1.deposit(deposit_amount)
        balance = deposit_amount

        print(f"Account balance for {account_number} is ${balance}")
        self.main_menu()


    def open_account(self):
        self.firstName = input("Enter first name: ")
        self.lastName = input("Enter last name: ")
        self.pin = input("Create PIN: ")

        account_number = self.bank.register_bank_account(self.firstName, self.lastName, self.pin)

        print(f"Hello, {self.firstName} {self.lastName}")
        print("Welcome to Tranxactrust. We are happy to help you with safe online payments.")
        print(f"Your account ID is: {account_number}")
        print(f"Your Tranxactrust wallet ID number is: {account_number}")

        self.main_menu()

if __name__ == "__main__":
    machine = ATMMachine()
    machine.main()
