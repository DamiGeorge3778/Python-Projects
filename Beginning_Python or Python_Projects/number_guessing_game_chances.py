# import
import random
# make variable
chances = 3
number_to_guess = random.randint(1, 100)
playing = True
# create loops and conditionals
while playing:
    print("You have " + str(chances) + " chances.")
    guess = input("Guess a number between 1 and 100: ")
    if guess != number_to_guess:
        chances -= 1
        print("")
        print("Wrong guess try again.")
        print("")
        if chances == 0:
            print("")
            print("Sorry you ran out of chances.")
            break
    # Tell the user they guessed it right
    if guess == number_to_guess:
        print("Good job you guessed the number!")
        break

    
