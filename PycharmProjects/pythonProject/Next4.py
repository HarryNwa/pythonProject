# for o in range(2, 12, 3):
#     for p in range(1, 12, 3):
#         print(p * 4, end=" ")


count = 0
num1 = 1
num2 = 1

first = " "
second = " "

while count<=10:
    if count <= 5:
        num1 = num1*4
        first = first+ " " + str(num1)

    if count <= 5:
        num2 = num2 * 8
        second = second + " " + str(num2)
    count+=1

print(first, end=" ")
print(second, end=" ")
