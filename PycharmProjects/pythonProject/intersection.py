test_list1 = (2, 4, 5, 6, 2)
test_list2 = (4, 2, 6, 7, 8)

res = tuple(set(test_list1).intersection(set(test_list2)))

print("The intersection is : " + str(res))
