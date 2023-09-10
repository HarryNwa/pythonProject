def number():
    user = input("Enter a number: ")
    if int(user) % 2 == 0:
        user = "Number is an even number"
    elif int(user) % 2 != 0:
        user = "Number is an odd number"

    print("Dear user: ", user)

number()