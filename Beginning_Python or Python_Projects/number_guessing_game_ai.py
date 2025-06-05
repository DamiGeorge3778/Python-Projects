# import
import random
number_to_guess = random.randint(1, 100)
# create loop
while True:
    guess = input("Guess a number between 1 and 100: ")
    if guess > str(number_to_guess):
        print("Too high!")
    if guess < str(number_to_guess):
        print("Too low!")
    if guess == str(number_to_guess):
        print("Good job, you guessed the number!")
        break