# class_name = "SS3"
# students_number = 0
# total = 0
# while students_number < 20:
#     score = int(input("Enter each student score here : "))
#
#     total = total + score
#     students_number = students_number +1
# average = total / students_number
# print('''*******************************************************************************
#                         Aso Rock Secondary School, Abuja, Nigeria
# *******************************************************************************''')
# print("Class: ", class_name, "\nNumber of Student in class: ", students_number, "\nTotal score: ", total, "\nAverage Score: ", average)
# print("*******************************************************************************")

#
# class_name = "SS3"
# students_number = 0
# total = 0
# while True:
#     score = int(input("Enter each student score here or -25 to exit: "))
#     if score == -25:
#         break
#     if score > 0:
#         total = total + score
#     students_number = students_number +1
# average = total / students_number
# print('''*******************************************************************************
#                         Aso Rock Secondary School, Abuja, Nigeria
# *******************************************************************************''')
# print("Class: ", class_name, "\nNumber of Student in class: ", students_number, "\nTotal score: ", total, "\nAverage Score: ", average)
# print("*******************************************************************************")




class_name = "SS3"
students_number = 0
total = 0
score = 0
score = int(input("Enter each student score here or -25 to exit: "))
while score != -25:
    total = total + score
    score = int(input("Enter each student score here or -25 to exit: "))
    # if score == -25:
    #     break
    # if score > 0:

    students_number = students_number +1
average = total / students_number
print('''*******************************************************************************
                        Aso Rock Secondary School, Abuja, Nigeria
*******************************************************************************''')
print("Class: ", class_name, "\nNumber of Student in class: ", students_number, "\nTotal score: ", total, "\nAverage Score: ", average)
print("*******************************************************************************")


# class_name = "SS3"
# students_number = 0
# total = 0
# # score = int(input("Enter each student score here or -25 to exit: "))
# for times in range(20):
#     score = int(input("Enter each student score here or -25 to exit: "))
#
#     total = total + score
#     students_number = students_number + 1
#     # if score == -25:
#     #     break
#     # if score > 0:
#
# average = total / students_number
# print('''*******************************************************************************
#                         Aso Rock Secondary School, Abuja, Nigeria
# *******************************************************************************''')
# print("Class: ", class_name, "\nNumber of Student in class: ", students_number, "\nTotal score: ", total, "\nAverage Score: ", average)
# print("*******************************************************************************")