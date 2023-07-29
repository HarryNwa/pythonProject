import random

number = random.randint(0, 50)
counter = 0

while counter <= 10:
    guess = int(input('Guess the number '))
    if guess == number:
        print('Congratulations! You guessed correctly')
        exit()
    else:
        print("try again")
    counter = counter + 1
    if counter == 10:
        print('Game over! You lost')
        exit()


