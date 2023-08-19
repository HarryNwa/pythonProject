# 5369020005703360
def validator():
    double_of_second_digit = 0
    card_type = ""
    card_holder = input("Hello kindly enter card details to verify ")

    if card_holder.startswith("4"): card_type = "VisaCard"

    elif card_holder.startswith("5"): card_type = "MasterCard"

    elif card_holder.startswith("37"): card_type = "America Express Card"

    elif card_holder.startswith("6"): card_type = "Discover Card"

    elif card_holder.startswith("50"): card_type = "Verve Card"

    for row in range(len(card_holder)):
        if row % 2 == 0:
            container = int(card_holder[row]) * 2

            if int(container) < 10:
                double_of_second_digit += container
            else:
                first_digit = container % 10
                second_digit = int(container / 10)
                double_of_second_digit += (first_digit + second_digit)

    sum_of_odd_places = 0
    for col in range(len(card_holder)):
        if col % 2 != 0:
            sum_of_odd_places = sum_of_odd_places + int(card_holder[col])

    total = sum_of_odd_places + double_of_second_digit
    if total % 10 == 0:
        validity = "Valid"
    else:
        validity = "Invalid"

    print(f"***Credit card type: {card_type}")
    print("***Credit Card Number: " + card_holder)
    print("***Credit Card Length: " + card_holder)
    print("***Credit Card Validity Status: " + validity)


validator()
