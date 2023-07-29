# int [] = int[3]
# numbers[0] = 44;
# numbers[1] = 23;
# numbers[2] = 2;
# System.out.println(Arrays.toString(numbers));


def divide_or_square(number: int):
    if number % 5 == 0:
        return number ** 0.5
    else:
        return number % 5


print(divide_or_square(9))

tuple = ("grace", 2, 2, True, [1, 2, 3], 10)


def is_even(x):
    return x % 2 == 0


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
answer = [i for i in list1 if i % 2 == 0]
add = [i for i in answer if list1]
ans = filter(is_even, list1)

print(answer)
print(sum(add))
print(ans)


def test2(x):
    return x % 2 == 0


t1 = (1, 3, 2, [1, 2, 3], 3)
x = t1[1] * t1[3]
x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x)
print(list(t1))
print(list(filter(test2, x1)))


def test3(n):
    return n ** 2


print(list(map(test3, x1)))


def test4(c):
    return c ** 2


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
com = [i for i in li if i ** 2]

# com = [c ** 2 for c in li]

print(list(map(test4, com)))

print(list(map(lambda y: y ** 2, li)))


def test5(a):
    return a % 2 == 0


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
com1 = [i for i in li if i % 2 == 0]

print(com1)


def is_pallindrome(show):
    for r in show[:: -1]:
        if show != show[:: -1]:
            return show == show[:: -1]


        else:
           return show


print(is_pallindrome("radar"))
