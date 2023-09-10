def big_list(num: int):
    double = []
    for i in range(num):
        double.append(i * 2)
    return double


print((big_list(10000)))


def generator_func(n):
    for x in range(n):
        yield x


g = generator_func(100)
for a in range(12):
    if a % 2 == 0:
        print(a)

# a = generator_func(1000)
#
#
# next(a)
# next(a)
# next(a)
# next(a)
#
# print(next(a))
