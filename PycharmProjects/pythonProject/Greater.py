# if number2 > number1 and number1 < number3 and number1 < number4:
#     maximum = number2
# if number3 > number2 and number2 < number1 and number2 < number4:
#     maximum = number3
# if number4 > number3 and number3 < number1 and number3 < number2:
#     maximum = number4
def greater(number1, number2, number3, number4):
    maximum = number1

    if number2 > maximum:
        maximum = number2
    if number3 > maximum:
        maximum = number3
    if number4 > maximum:
        maximum = number4
    # return maximum
    print(maximum)
    minimum = number1
    if number2 < minimum:
        minimum = number2
    if number3 < minimum:
        minimum = number3
    if number4 < minimum:
        minimum = number4
    # return minimum
    print(minimum)

greater(231, 543, 143, 87)


x = 2



# def greater():
#     x =1
#     x += 1
#     return x
#
#
#
# print(greater())
# print(greater())
# print()


# for r in range(1, 11):
#     print(r, end=" ")

















