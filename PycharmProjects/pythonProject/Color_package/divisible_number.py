def divisible():
    number = int(input("Enter number"))

    if number >= 1500 and number == 2700:
        if number % 7 == 0:
            num = number
            if num / 5 == 0:
                print(num)

divisible()