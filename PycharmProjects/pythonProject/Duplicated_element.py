duplicate = [3, 2, 4, 4, 4, 12, 32, 8, 6, 9, ]
me = "Harry"

def numeric(selector):
    new_member = []
    for element in selector:
        if element not in new_member:
            new_member += [element]
    return new_member


print(numeric(duplicate))
print(me)

# select = [3, 2, 4, 4, 4, 12, 32, 8, 6, 9, ]
# select = set(select)
# select = list(select)
# print(select)


counted = [(4, 4, 12), [32, 8, 6], 9, 1, {3, 2, 5, 12}]


def box(counted):
    counter = 0
    for number in counted:
        counter += 1
    return counter


print(box(counted))

