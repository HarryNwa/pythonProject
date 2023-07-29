# passes = 0
# failures = 0
# for student in range(10):
#     result = int(input('Enter result (1=pass, 2=fail): '))
#     if result == 1:
#         passes = passes + 1
#     if result == 2:
#         failures = failures + 1
#     if result != 1 or 2:
#         continue
# else:
#     failures = failures + 1
# print('Passed:', passes)
# print('Failed:', failures)
# # if passes > 8:
# #     print('Bonus to instructor')
#
#
# a = b = 7
# print("a =", a, "\nb =", b)
#
#
# for row in range(10):
#     for column in range(10):
#         print('<' if row % 2 == 1 else '>', end='')
#     print()
#
#
# for row in range(2):
#     for column in range(7):
#         print('@' if row % 2 == 1 else "@", end="")
#     print()



# passes = 0
# failures = 0
# counter = 0
# for student in range(10):
#     result = int(input('Enter result (1=pass, 2=fail): '))
#     if result == 1:
#         passes = passes + 1
#     if result == 2:
#         failures = failures +2
#     if result != 1 or 2:
#         continue
# else:
#     print('Passed:', passes)
#     print('Failed:', failures)
# # counter = counter + 1
# # if counter == 10:
# #     print(counter)
from xmlrpc.client import boolean
#
# print('Enter two integers, and I will tell you', 'the relationships they satisfy.')
#
# number1 = int(input('Enter first integer: '))
#
# number2 = int(input('Enter second integer: '))
# if number1 == number2:
#     print(number1, 'is equal to', number2)
# else:
#     print(number1, 'is not equal to', number2)
# if number1 < number2:
#     print(number1, 'is less than', number2)
# else:
#     print(number1, 'is greater than', number2)
# if number1 <= number2:
#     print(number1, 'is less than or equal to', number2)
# else:
#     print(number1, 'is greater than or equal to', number2)


# question = boolean(input("What is your problem? "))
# if question == True:
#     question2 = input("Have you had this problem before (Yes? No?) ")
# if question == True:
#     print("Well you have it again")
# else:
#     print("Well, you have it now ")

#
# print("Number \tsquare \t  cube")
# for number in range(21):
#     print(f" {number}\t\t{number * number}\t\t\t{number * number * number}", end="\n")

# sun = 0
# product = 0
# smallest = 0
# largest = 0
# number = 0
#
# for number in range(3):
#     sum = number + 1
#     user = int(input("Enter number "))
#
#     product = product * sum
#     smallest = sum < user
#     largest = largest > user
#     number = number + 1
# average = number/ sum
# print(sum, average, product, smallest, largest)



# for num in range(2):
#     num = num + 1
# percentage_invest = int(input("Enter a number in percentage "))
# start_amount = int(input("Enter a amount "))
# years_after = int(input("Enter accumulated years "))
#
# number_of_years = start_amount * ((1 + (percentage_invest/100))**years_after)
# print("Money made in  " + str(years_after) + " years is " + str(number_of_years))



# miles = 0
# gallons = 0
# total = 0
# sumTotal = 0
# totalMiles = 0
# totalGallons = 0
# gallons = float(input("Enter the gallons used: "))
# miles = float(input("Enter the miles driven: "))
# while gallons != -25:
#     totalMiles = totalMiles + miles
#     totalGallons = totalGallons + gallons
#     total = total + 1
#     average = miles / gallons
#     sumTotal = sumTotal + average
#     print("The overall average was ", average)
#     gallons = float(input("Enter the gallons used: "))
#     miles = float(input("Enter the miles driven: "))
# sumTotal = sumTotal / total
# totalCombo = totalMiles / totalGallons
# print("Combined miles driven is ", totalCombo)
# print("Total average is ", sumTotal)



# print("(a)\t\t(b)\t\t(c)\t\t(d)")
# for row in range(4):
#     if row == 1:
#         print("*", end="")
#     else:
#         row = "*" * 1
#         print(row, end="\t")
#     print(" ")
#     if row == 2:
#         print(row, end="")
#     else:
#         row = "*" * 2
#         print(row, end="\t")
#     print(" ")
#     if row == 3:
#         print(row, end="")
#     else:
#         row = "*" * 3
#         print(row, end="\t")
#     print(" ")
#     if row == 4:
#         print(row, end="")
#     else:
#         row = "*" * 4
#         print(row, end="\t")
#     print(" ")
#     if row == 5:
#         print(row, end="")
#     else:
#         row = "*" * 5
#         print(row, end="\t")
#     print(" ")
#     if row == 6:
#         print(row, end="")
#     else:
#         row = "*" * 6
#         print(row, end="\t")
#     print(" ")
#     if row == 7:
#         print(row, end="")
#     else:
#         row = "*" * 7
#         print(row, end="\t")
#     print(" ")
#     if row == 8:
#         print(row, end="")
#     else:
#         row = "*" * 8
#         print(row, end="\t")
#     print(" ")
#     if row == 9:
#         print(row, end="")
#     else:
#         row = "*" * 9
#         print(row, end="\t")
#     print(" ")
#     if row == 10:
#         print(row, end="")
#     else:
#         row = "*" * 10
#         print(row, end="\t")
#         print(" ")



# function which return reverse of a string

# def isPalindrome(s):
# 	return s == s[::-1]
#
#
#
# s = "123421"
# ans = isPalindrome(s)
#
# if ans:
# 	print("Yes")
# else:
# 	print("No")



for counter in range (5):
    for number in range(counter+1):
        if counter > 1:
            counter = counter -1
            number = number * counter
    print(number)