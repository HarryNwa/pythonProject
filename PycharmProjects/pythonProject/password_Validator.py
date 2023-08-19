import re


def validate_password():

    while True:

        passwrd = input("Enter password: ")

        if len(passwrd) < 8:
            print("Invalid password. Password must contain at least 8 characters, \nincluding at least one upper "
          "case letter, one lower case letter, \none special character and one numerical figure.")
            continue

        if not re.search("[A-Z]", passwrd):
            print("Invalid password. Password must contain at least 8 characters, \nincluding at least one upper "
          "case letter, one lower case letter, \none special character and one numerical figure.")
            continue

        if not re.search(r"[a-z]", passwrd):
            print("Invalid password. Password must contain at least 8 characters, \nincluding at least one upper "
          "case letter, one lower case letter, \none special character and one numerical figure.")
            continue

        if not re.search(r"[0-9]", passwrd):
            print("Invalid password. Password must contain at least 8 characters, \nincluding at least one upper "
          "case letter, one lower case letter, \none special character and one numerical figure.")
            continue

        if not re.search(r"[@_!#$%^&*()<>?}{~:=-]", passwrd):
            print("Invalid password. Password must contain at least 8 characters, \nincluding at least one upper "
          "case letter, one lower case letter, one special character and one numerical figure.")
            continue

        return True


if validate_password():
    print("Valid password")
