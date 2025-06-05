# create input
number = input("Enter a number to guess: ")
# print 100 lines
print("\n" * 100)
# create loop and conditions
while True:
    guess = input("Guess a number between 1 and 100: ")
    if guess > number:
        print("Too high!")
    if guess < number:
        print("Too low!")
    if guess == number:
        print("Good job, you guessed the number!")
        break