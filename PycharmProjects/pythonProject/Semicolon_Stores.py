# create static variable for item names
# create another that counts the units bought
# create another that stores the cost of item
# collect the name of the cashier
# create a nested for loop under a new method, and print the table filler
# loop through the counting variable and display the quantity bought and price
# sout and collect payment
# if payment is above total expenses, minus total expenses from payment
# include pay in the receipt and print with thank you for your patronage
import re
from datetime import datetime
storeName = "SEMICOLON STORES"
branch = "MAIN BRANCH"
location = "LOCATION: 312, HERBERT MACAULAY WAY, SABO YABA, LAGOS"
phone = "TEL: +2348034586387"
customer = []
check_item = []
item_count = []
item_price = []
cashier = []
discount = 0
current_time = datetime.now().time()
sub_total = 0
total = 0
bill_total = 0
total_minus_discount = 0
vat = 0
balance = 0
# new_balance = 0
def item_checkout():
    global customer
    while True:
        try:
            customer_name = input("What is customer's name? ")
            if re.search("\\D*", customer_name):
                customer.append(customer_name)
                item_name()
            else:
                 print("Wrong input. Please retry.")
                 item_checkout()

        except(ValueError, KeyboardInterrupt):
            print("Invalid input")
            item_checkout()

def item_name():
    global check_item
    while True:
        try:
            item = input("What did the user buy? ")
            if not re.search("^[0-9]\\d*", item):
                check_item.append(item)
                item_unit()
            else:
                print("Wrong input. Please retry")

        except(ValueError, KeyboardInterrupt):
            print("Invalid input")
            # item_name()
        break
    item_name()


def item_unit():
    while True:
        try:
            cart_unit = input("How many pieces? ")
            if re.search(r'^-?\d+$', cart_unit):
                if int(cart_unit) > 0:
                    item_count.append(int(cart_unit))
                    price_per_unit()
            else:
                print("Invalid input")

        except(ValueError, KeyboardInterrupt):
            print("Invalid value")
            break
        item_unit()


def price_per_unit():
    while True:
        try:
            cost_price = input("How much per unit? ")
            if re.match(r'^-?\d+$', cost_price):
                if int(cost_price) > 0:
                    item_price.append(int(cost_price))
                    more_items()
            else:
                print("Invalid amount")
                price_per_unit()
        except(ValueError, KeyboardInterrupt):
            print("Invalid input")


def more_items():
    choice1 = "Yes".lower()
    choice2 = "No".lower()
    while True:
        try:
            more_item = input("Add more items? ").lower()
            if re.search("\\D*", more_item):
                if more_item == choice1:
                    item_name()
                if more_item == choice2:
                    cashier_name_box()
            else:
                print("Invalid choice")
                more_items()
        except(ValueError, KeyboardInterrupt):
            print("Invalid input")
            more_items()

def cashier_name_box():
    while True:
        try:
            cashier_name = input("What is your name? ")
            if re.search("\\D*", cashier_name):
                cashier.append(cashier_name)
                percentage_discount()
            else:
                print("Name is not taken. Please enter a valid name")
                cashier_name_box()
        except(ValueError, KeyboardInterrupt):
            print("Invalid input")





def percentage_discount():
    global discount
    while True:
        try:
            unit_discount = input("How much discount will he get? ")
            if re.match(r'^-?\d+$', unit_discount):
                discount = int(unit_discount)
                receipt_print()
            else:
                print("Invalid rate")
                percentage_discount()
        except(ValueError, KeyboardInterrupt):
            print("Invalid input")

def receipt_print():
    global sub_total
    global total
    print(storeName + "\n" + branch + "\n" + location + "\n" + phone)
    print("Time: ", current_time)
    print("Cashier: " + cashier[0] + "\nCustomer Name: " + customer[0])
    print("=" * 50)
    print("ITEM\t\t" + "QTY" + "\t\tPRICE" + "\t\tTOTAL(NGN)")
    print("-" * 50)

    for row in range(len(check_item)):

        total = item_count[row] * item_price[row]
        print(check_item[row], "\t\t", item_count[row], "\t\t", item_price[row], "\t\t", total)
        sub_total += total

    actual_discount_and_VAT()

def actual_discount_and_VAT():
    global sub_total
    global bill_total
    global vat
    global total_minus_discount
    print("-" * 50)
    current_discount = discount / 100
    total_minus_discount = sub_total * current_discount

    current_vat = (17.5 / 100) * sub_total
    vat = current_vat

    print("Sub Total:\t ", sub_total, "\nDiscount:\t ", total_minus_discount, "\nVAT @ 17.5:\t ", vat)
    print("=" * 50)
    bill_total = sub_total + total_minus_discount + vat
    print("Bill Total:\t ", bill_total)
    print("THIS IS NOT AN RECEIPT PAY ", bill_total)
    print("=" * 50)

    amount_paid_and_balance()


def amount_paid_and_balance():
    global balance
    while True:
        try:
            paid_amount = input("\n\nHow much did the customer give you?")
            if re.match(r'^-?\d+$', paid_amount):
                if int(paid_amount) >= 0:
                    balance = int(paid_amount)
                    print_receipt()
                else:
                    print("Invalid rate")
                    percentage_discount()
        except(ValueError, KeyboardInterrupt):
            print("Invalid input")
            break


def print_receipt():
    global balance
    global bill_total
    global cashier
    global customer
    global sub_total
    global total_minus_discount
    global balance
    global total
    new_balance = balance - bill_total

    print(storeName + "\n" + branch + "\n" + location + "\n" + phone)
    print("Time: ", current_time)
    print("Cashier: " + cashier[0] + "\nCustomer Name: " + customer[0])
    print("=" * 50)
    print("ITEM\t\t" + "QTY" + "\t\tPRICE" + "\t\tTOTAL(NGN)")
    print("-" * 50)


    for col in range (len(check_item)):

        total = item_count[col] * item_price[col]
        print(check_item[col], "\t\t", item_count[col], "\t\t", item_price[col], "\t\t", total)
        sub_total += total

    print("\n" + "-" * 50)
    print("Sub Total:\t ", sub_total, "\nDiscount:\t ", total_minus_discount, "\nVAT @ 17.5:\t ", vat)
    print("\n" + "=" * 50)

    bill_total = sub_total + total_minus_discount + vat
    print("Bill Total:\t ", bill_total, "\nAmount Paid: ", balance, "\nBalance: ", new_balance)
    print("=" * 50)
    print("THANK YOU FOR YOUR PATRONAGE")
    print("=" * 50)


item_checkout()
item_name()
item_unit()
price_per_unit()
more_items()
cashier_name_box()
receipt_print()
actual_discount_and_VAT()
amount_paid_and_balance()