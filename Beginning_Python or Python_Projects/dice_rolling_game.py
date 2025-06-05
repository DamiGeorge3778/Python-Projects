# import
import random
# create variables and input and loop
while True:
    question = input("Do you want to roll the dice? (y/n): ").lower()
    if question == "n":
        print("Aw man, ok.")
        break
    dice_roll = random.randint(1, 6)

    extra = "("

    extra2 = ")"

    extra3 = ", "

    dice_roll2 = random.randint(1, 6)
    # create condintionals
    if question == "y":
        print("Ok! You rolled a " + extra + str(dice_roll) + extra3 + str(dice_roll2) + extra2)
        
    if question != "y" and question != "n":
        print("Invaild choice, try again.")
        continue
    again = input("Would you like to play again? ")
    if again == "yes" or again == "y":
        print("Ok!")
        continue
    if again == "no" or again == "n":
        print("Alright thats fine, thanks for playing!")
        break