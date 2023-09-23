list1 = [3, 4, 9, 7, 2, 0]


def sum_list(lst, value):
    for add in range(len(list1)):
        for added in range(1, len(list1)):
            if lst[add] + lst[added] == value:
                return [add, added]


print(sum_list(list1, 16))


l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]


def creating_tuple(lst1, lst2):
    # return list(zip(lst1, lst2))

    num = []
    for all in range(len(lst1)):
        figure = lst1[all], lst2[all]
        num.append(figure)
    return num


print(creating_tuple(l1, l2))


l3 = [1, 2, 3, 4, 5]
l4 = [6, 7, 8, 9, 10, 11]


def creating_tuple(lst1, lst2):
    num = []
    for all in range(len(lst1)):
        figure = lst1[all], lst2[all]
        num.append(figure)


print(creating_tuple(l3, l4))