import math


def area_of_circle(radius):
    if radius < 0:
        raise ValueError
    if type(radius) is not int and type(radius) is not float:
        raise TypeError
    return math.pi * (radius ** 2)
    # area = math.pi * (radius ** 2)
    # print(float(area))


result = area_of_circle(4)
print(result)
