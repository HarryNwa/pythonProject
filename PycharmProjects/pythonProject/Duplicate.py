# create a function
# create a variable of an empty list
# loop through the lists
# return length of list not found in loop
# provide the lists to be looped through
# print whether there is a duplicate
# print whether there is no duplicate
def check_duplicate(doubly):
    found = []

    checker = [r for r in doubly if r not in found and not found.append(r)]
    return len(doubly) != len(checker)


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

print("There is a duplicate:", check_duplicate(fruits))
print("There is no duplicate:", check_duplicate(names))
