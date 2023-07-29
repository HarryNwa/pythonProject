# create a list
# create a function
# give the function a parameter
# loop through the list
# create an if statement for finding odd number
# compare each odd numbers in the list
# return the highest odd number in the list



def highest_odd(lit):
    highest_odd_number = None
    for number in lit:
        if number % 2 != 0 and (highest_odd_number is None or number > highest_odd_number):
            highest_odd_number = number

    return highest_odd_number

listing = [34, 5, 69, 109, 78, 93, 10]
# call = highest_odd(listing)
print(highest_odd(listing))


set1 = {1, 2, 2, 3, 3, (1, 1, 2, 3)}

print(set1)
