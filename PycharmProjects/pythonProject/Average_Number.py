
positive = 0
negative = 0
total = 0
calculated = 0


while (True):
    integer = float(input("Enter your number: "))

    if integer == 0:
        break

    calculated = calculated + integer
    total = total + 1

    if integer < 0:
        negative = negative + 1

    if integer > 0:
        positive = positive + 1

average = calculated/total

print("The number of positives is ", positive)
print("The number of negatives is ", negative)
print("The total is ", calculated)
print("The average is ", average)


