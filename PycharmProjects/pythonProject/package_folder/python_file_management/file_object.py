with open("account.txt", mode="r") as my_file:
    my_file.read()

with open("account.txt", mode="w") as my_file:
    my_file.write("001 esther 15\n")
    my_file.write("002 peter 35\n")
    my_file.write("003 victor 24\n")
    my_file.write("004 moyin 16\n")
    my_file.write("005 grace 19\n")


with open("account.txt", mode="r") as my_file:
    print(my_file.read())






