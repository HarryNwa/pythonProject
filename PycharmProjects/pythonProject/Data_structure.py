# my_list = [1, 2, 3, 3, 4, 5, True, "chisom", 3.2, "tobi"]
# print(id(my_list))
# new_list = my_list[7] = "seyi"
#
# l1 = [1, 3, 4, 3, 3]
# l2 = [4, 5, 5, 6]
# l3 = l1 + l2
#
#
# print(my_list)
# print(id(new_list))
#
#
# for item in range(len(l1)):
#     l1[item] = l1[item] ** 2
#     print(l1)


numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]
# print(numbers[::-1])

result = []
for row in range(len(numbers)-1,-1,-1):
    result.append(numbers[row])
print(result)


def sorted_list(item):
    for i in range(len(item)):
        for j in range(len(item)):
            if item[j] > item[i]:
                item[j], item[i] = item[i], item[j]
    return item
print(sorted_list(numbers))


def even_number(list):
    new_list = []
    for number in list:
        if number % 2 == 0:
            new_list.append(number)
    return new_list


result = [i for i in numbers if i % 2 == 0]
print(even_number(numbers))
print(result)


def sorted_list(item):
    for i in range(len(item)):
        for j in range(len(item)):
            if item[i] > item[j]:
                item[i], item[j] = item[j], item[i]
    return item
print(sorted_list(numbers))


# numbers = [8, 2, 5, 6, 1, 3, 9, 4, 7]
# for item in numbers[0:]:
#     if 0 > 1:
#         numbers[4]
# print(numbers[4])
# for item in numbers:
#     if 1 > 2:
#         numbers[1]
# print(numbers[1])
# for item in numbers:
#     if 2 > 3:
#         numbers[5]
# print(numbers[5])
# for item in numbers:
#     if 3 < 4:
#         numbers[7]
# print(numbers[7])
# for item in numbers:
#     if 4 < 5:
#         numbers[2]
# print(numbers[2])
# for item in numbers:
#     if 5 > 6:
#         numbers[3]
# print(numbers[3])
# for item in numbers:
#     if 6 > 7:
#         numbers[8]
# print(numbers[8])
# for item in numbers:
#     if 7 < 8:
#         numbers[0]
# print(numbers[0])
#
# print(" ", end="")


    #     sort()
    # # if numbers[0 > 1 and 1<2 or 2<3 or 3<4 or 4<5 or 5<6 or 6<7 or 7<8]:
    #     print(numbers)


# numbers = [10, 20, 30, 40, 50]
# for item in range(len(numbers)):
#     numbers[item] = numbers[item] ** 2
# print(numbers)



