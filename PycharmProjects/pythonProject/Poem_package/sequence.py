def user():
    global check
    global checker
    numbers = (input("Enter numbers: "))

    check = [numbers]
    checker = (numbers)

    print("List: ", check)
    print("Tuple: ", checker)

user()