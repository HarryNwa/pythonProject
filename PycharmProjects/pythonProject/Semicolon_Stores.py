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


def item_checkout():
    global customer
    try:
        customer_name = input("What is customer's name? ")
        if re.fullmatch("\\D*", customer_name):
            customer.append(customer_name)
            item_name()
        else:
            raise ValueError

    except(ValueError, KeyboardInterrupt):
        print("Invalid input")
        item_checkout()


def item_name():
    global check_item
    try:
        item = input("What did the user buy? ")
        if not re.search("^[0-9]\\d*", item):
            check_item.append(item)
            item_unit()
        else:
            print("Wrong input. Please retry")

    except(ValueError, KeyboardInterrupt):
        print("Invalid input")
        item_name()


def item_unit():
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
        item_unit()


def price_per_unit():
    try:
        cost_price = input("How much per unit? ")
        if re.match(r'^-?\d+$', cost_price):
            if int(cost_price) > 0:
                item_price.append(int(cost_price))
                more_items()
        else:
            raise ValueError
    except(ValueError, KeyboardInterrupt):
        print("Invalid Amount")
        price_per_unit()


def more_items():
    choice1 = "Yes".lower()
    choice2 = "No".lower()
    try:
        more_item = input("Add more items? ").lower()
        if re.search("\\D*", more_item):
            if more_item == choice1:
                item_name()
            if more_item == choice2:
                cashier_name_box()
        else:
            raise ValueError

    except(ValueError, KeyboardInterrupt):
        print("Invalid input")
        more_items()


def cashier_name_box():
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
    try:
        unit_discount = input("How much discount will he get? ")
        if re.match(r'^-?\d+$', unit_discount):
            discount = int(unit_discount)
            receipt_print()
        else:
            raise ValueError
    except(ValueError, KeyboardInterrupt):
        print("Invalid input")
        percentage_discount()


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

    actual_discount_and_vat()


def actual_discount_and_vat():
    global sub_total
    global bill_total
    global vat
    global total_minus_discount
    print("-" * 50)
    current_discount = discount / 100
    total_minus_discount = current_discount * sub_total

    current_vat = (17.5 / 100)
    vat = current_vat * sub_total

    print("Sub Total:\t ", sub_total, "\nDiscount:\t ", total_minus_discount, "\nVAT @ 17.5:\t ", vat)
    print("=" * 50)
    bill_total = sub_total - total_minus_discount + vat
    print("Bill Total:\t ", bill_total)
    print("=" * 50)
    print("THIS IS NOT AN RECEIPT PAY ", bill_total)
    print("=" * 50)

    amount_paid_and_balance()


def amount_paid_and_balance():
    global balance
    try:
        paid_amount = input("\n\nHow much did the customer give you?")
        if re.match(r'^-?\d+$', paid_amount):
            if int(paid_amount) >= 0:
                balance = int(paid_amount)
                print_receipt()
            else:
                raise ValueError
    except(ValueError, KeyboardInterrupt):
        print("Invalid input")
        amount_paid_and_balance()


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

    for col in range(len(check_item)):
        total = item_count[col] * item_price[col]
        print(check_item[col], "\t\t", item_count[col], "\t\t", item_price[col], "\t\t", total)

    print("\n" + "-" * 50)
    print("Sub Total:\t ", sub_total, "\nDiscount:\t ", total_minus_discount, "\nVAT @ 17.5:\t ", vat)
    print("\n" + "=" * 50)

    print("Bill Total:\t ", bill_total, "\nAmount Paid: ", balance, "\nBalance: ", new_balance)
    print("=" * 50)
    print("THANK YOU FOR YOUR PATRONAGE")
    print("=" * 50)


item_checkout()

