# weight = float(input("Enter weight "))
# price = float(input("Enter price "))
# weightOne = float(input("Enter weight "))
# priceTwo = float(input("Enter price "))
#
# parcelOne = weight/price
# parcelTwo = weightOne / priceTwo
# if parcelOne < parcelTwo:
#     print("Package 2 has a better price ", f"{parcelTwo:.2f}")
# else:
#     print("Package 1 has a better price ", f"{parcelOne:.2f}")


divideInteger = int(input("Enter number "))
if (divideInteger % 5 == 0) and (divideInteger % 6 == 0):
    print("Is ", divideInteger, " divisible by 5 and 6?", True)
else:
    print("Is ", divideInteger, " divisible by 5 and 6?", False)
if (divideInteger % 5 == 0) or (divideInteger % 6 == 0):
    print("Is ", divideInteger, " divisible by 5 or 6?", True)
else:
    print("Is ", divideInteger, " divisible by 5 or 6?", False)
if (divideInteger % 5 == 0) ^ (divideInteger % 6 == 0):
    print("Is ", divideInteger, " divisible by 5 or 6, but not both?", True)
else:
    print("Is ", divideInteger, " divisible by 5 or 6, but not both?", False)
