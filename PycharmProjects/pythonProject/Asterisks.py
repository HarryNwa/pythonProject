# print("(a)\t\t\t\t\t(b)\t\t\t\t\t(c)\t\t\t\t\t(d)\t\t\t\t\t(e)")
#
# for a in range(1, 6):
#     for b in range(1, 6):
#         print(a**b, end="\t\t\t\t\t")
#     print()


digits = int(input("Enter a number "))

digit_1 = digits // 1000
digit_2 = (digits % 1000) // 100
digit_3 = (digits % 100) // 10
digit_4 = digits % 10
total = digit_1 + digit_2 + digit_3 + digit_4
print(digit_1, digit_2, digit_3, digit_4)
print("The sum is ", total)

# def triangle(size):
#     for a in range(size):
#         for b in range(a+1):
#             print("#", end=" ")
#         for c in range(size - a):
#             print(" ", end=" ")
#         for d in range(size - a):
#             print("#", end=" ")
#         for e in range(a+1):
#             print(" ", end=" ")
#         for f in range(a+1):
#             print(" ", end=" ")
#         for g in range(size - a):
#             print("#", end=" ")
#         for h in range(size-a):
#             print(" ", end=" ")
#         for i in range(a+1):
#             print("#", end=" ")
#
#         print()
#
#
# if __name__ == '__main__':
#     triangle(10)
