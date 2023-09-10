with open("archive.txt", mode="r") as user_file:
    user_file.read()

    with open("archive.txt", mode="w") as user_file:
        user_file.write("Semicolon admission letter\n")
        user_file.write("Company registration document\n")
        user_file.write("Users tracker\n")
        user_file.write("Yearly revenue\n")
        user_file.write("Awards and prizes\n")

    with open("archive.txt", mode="r") as user_file:
        print(user_file.read())