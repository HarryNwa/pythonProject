list1 = ["dfa12321afd"]
# list2 = (eval(i) for i in list1)


def second_largest(finder):
    number = []

    second = 1
    for large in range(len(finder)):
        if large in list1 not in number:
            second = large
            return second


print(second_largest(list1))
