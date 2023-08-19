while True:
    try:
        num1, num2 = eval(input("Enter a number separated by comma: "))
        result = num1 / num2
        print(result)
    except (SyntaxError, ZeroDivisionError):
        print("Enter a number separated by comma: ")
    # except ZeroDivisionError:
    #     print("You cannot divide by zero")
    else:
        print("Thank you for using my calculated.")
        break
    finally:
        print("The exception has been handled.")
