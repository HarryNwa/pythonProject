# class BankAccount:
#     def __init__(self, account_number, user_name, pin):
#         self.account_number = account_number
#         self.user_name = user_name
#         self.pin = pin
#         self.balance = 0.0
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: ${amount}")
#         else:
#             print("Invalid deposit amount.")
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawn: ${amount}")
#         else:
#             print("Invalid withdrawal amount or insufficient balance.")
#
#     def get_balance(self):
#         return self.balance
#
#     def account_deposit(self, amount):
#         self.balance += amount
#
#     def account_withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Invalid withdrawal amount or insufficient balance.")
from BankApp.bank import Bank
from BankApp.account import Account

# class Bank:
#     def __init__(self, name):
#         self.name = name
#
#     def generate_account_number(self):
#         # You can implement your own logic to generate account numbers
#         pass
#
#     def register(self, first_name, last_name, pin):
#         # You can implement registration logic here
#         pass
#
#     def find_account(self, account_number):
#         # You can implement account lookup logic here
#         pass

if __name__ == "__main__":
    def welcome_menu():
        print("HELLO! WELCOME TO TRANXACTRUST\n")
        print("1. Create a free account")
        print("2. Log in")
        print("3. Exit")
        user_input = input("Enter your choice: ")

        if user_input == '1':
            open_account()
        elif user_input == '2':
            login()
        elif user_input == '3':
            exit_diary()
        else:
            exit(0)

    def exit_diary():
        exit_option = input("Click 'yes' to log out or 'no' to return to the app menu: ")
        if exit_option.lower() == 'yes':
            print(":( Tranxactrust app is closing...\nGoodbye!")
            exit(0)
        elif exit_option.lower() == 'no':
            welcome_menu()
        else:
            exit(0)

    def login():
        try:
            user_login = input("Enter username: ")
            user_password = input("Enter password: ")

            if user_login != user_name or user_password != pin:
                print("Invalid username or password")
                login()
            else:
                print("Login successful")
                main_menu()
        except Exception as error:
            print(error)
            welcome_menu()

    def main_menu():
        print("Welcome to Tranxactrust!\n")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check balance")
        print("5. Logout")
        user_input = input("Enter your choice: ")

        if user_input == '1':
            deposit()
        elif user_input == '2':
            withdraw()
        elif user_input == '3':
            transfer()
        elif user_input == '4':
            check_balance()
        elif user_input == '5':
            logout()
        else:
            exit(0)

    def logout():
        logout_option = input("Click 'yes' to log out or 'no' to return to the app menu: ")
        if logout_option.lower() == 'yes':
            welcome_menu()
        elif logout_option.lower() == 'no':
            main_menu()
        else:
            exit(0)

    def check_balance():
        print(f"Account balance for {name} is ${bank1.get_balance()}")
        main_menu()

    def transfer():
        receiver_account_number = input("Enter receiver account number: ")
        amount = float(input("Enter amount: "))
        bank1.account_deposit(amount)
        bank1.account_withdraw(amount)

        receiver_account = bank.find_account(receiver_account_number)
        balance = amount

        print(f"Dear {first_name} {last_name}, you received ${amount} from {receiver_account.user_name}. "
              f"Your account balance with account number {receiver_account_number} is ${balance}")
        main_menu()

    def withdraw():
        withdrawer_number = input("Enter account number: ")
        amount = float(input("Enter amount: "))
        bank1.account_deposit(amount)
        bank1.account_withdraw(amount)

        withdrawer_account = bank.find_account(withdrawer_number)
        balance = amount

        print(f"Dear {first_name} {last_name}, ${amount} was debited from your account balance "
              f"with account number {withdrawer_number}. Your balance is ${balance}")
        main_menu()

    def deposit():
        deposit_amount = float(input("Enter amount: "))
        account_number = input("Enter account number: ")

        bank1.deposit(deposit_amount)
        balance = deposit_amount

        print(f"Account balance for {account_number} is ${balance}")
        main_menu()

    def open_account():
        global first_name, last_name, user_name, pin, name, bank1
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        pin = input("Create pin: ")

        user_name = first_name + " " + last_name
        name = f"Hello, {first_name} {last_name}, welcome to Tranxactrust. We are happy to help you with safe online payments."

        print(name)

        account_number = bank.generate_account_number()
        account = account_number
        bank.register_bank_account(first_name, last_name, pin)
        bank1 = Account(account, user_name, pin)

        print(f"Dear {first_name} {last_name}, your account ID is: {account_number}")
        print(f"Your Tranxactrust wallet ID number is: {account_number}")

        main_menu()

    bank = Bank("Tranxactrust")
    first_name = ""
    last_name = ""
    user_name = ""
    pin = ""
    name = ""
    bank1 = Account("", "", "")
    welcome_menu()
