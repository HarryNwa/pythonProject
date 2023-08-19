import random
#
# number = random.randint(0, 50)
# counter = 0
#
# while counter <= 10:
#     guess = int(input('Guess the number '))
#     if guess == number:
#         print('Congratulations! You guessed correctly')
#         exit()
#     else:
#         print("try again")
#     counter = counter + 1
#     if counter == 10:
#         print('Game over! You lost')
#         exit()

# # def game(counter):
# number = random.randint(0, 100)
# counter = 0
#
# while counter <= 10:
#     guess = int(input('Guess the number '))
#     if guess > 1 or guess < 56:
#         print("Too low. Try again")
#
#     if guess > 58 or guess <= 100:
#         print("Too high. Try again")
#
#     if guess == 57:
#         print('Congratulations! You guessed correctly')
#         exit()
#     # counter = counter + 1
#     if counter == 10:
#         print('Game over! You lost')
#         exit()


# for n in range(1, 100):
#     if n % 3 == 0 and n % 5 == 0:
#         print("Fizz Buzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     elif n % 5 == 0:
#         print("Buzz")
#
#     else:
#         print(n)



checker = int(input("What is your height? "))

if checker >= 6:
    print("You're eligible to dive.")
else:
    print("You are below the height of eligibility")

ageCheck = int(input("What is your age? "))

if ageCheck <= 12:
    print("Your charge pay N100")

if ageCheck >= 12 and ageCheck <= 60:
    print("Your charge is N200")

if ageCheck > 60:
    print("Your charge is FREE")
    exit()


