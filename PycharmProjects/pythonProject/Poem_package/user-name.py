def name():
    name_box = []
    user = input("Enter first name and last name: ")

    for a in user:
        name_box.append(a)

    print(name_box[::-1])

name()
