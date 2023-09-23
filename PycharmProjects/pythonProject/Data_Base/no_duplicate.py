# lst = [2, 2, 1]
# lst1 = [3, 3, 2, 4, 3, 3]
# lst2 = [1]
#
#
# def single_number(selector: []):
#     num = 0
#
#     for number in range(len(selector)):
#         sort = 0
#         for numbers in range(len(selector)):
#             if selector[number] == selector[numbers]:
#                 sort += 1
#         if sort <= 1:
#             num = selector[number]
#     return num
#
#
# print(single_number(lst))
# print(single_number(lst1))
# print(single_number(lst2))

input1 = [5, 7, 15, 1, 10]


def largest_difference(select: []):
    numb = []
    for element in range(len(select)):
        count = 0
        for number in range(len(select)):
            if select[element] - select[number]:
                count += 1
            if count <=1:
                numb = select[element] - select[number]
        return numb


print(largest_difference(input1))
