# create loop variable
calculating = True
# create greeting function
def welcome():
    print("Hi there, welcome to my calculator!") 
welcome()
# create input
while calculating:
    enter = input("What type of mathmatical operation would you like to perform? ").lower()
# create addition conditional
    if enter == "addition" or enter == "a":
        addition1 = input("What is the first number you would like to add together? ")
        
        addition2 = input("What is the second number you would like to add together? ")
        
        add_total = int(addition1) + int(addition2)
        
        print("Your final added total is " + str(add_total))
    # create subtraction conditional
    if enter == "subtraction" or enter == "s":
        subtraction1 = input("What is the first number you would like to subtract? ")
        
        subtraction2 = input("What is the second number you would like to subtract? ")
        
        subtract_total = int(subtraction1) - int(subtraction2)
        
        print("Your final subtracted total is " + str(subtract_total))
    # create multiplication conditional
    if enter == "multiplication" or enter == "m":
        multiplication1 = input("What is the first number you would like to multiply? ")
        
        multiplication2 = input("What is the second number you would like to multiply? ")
        
        multiply_total = int(multiplication1) * int(multiplication2)
        
        print("Your final multiplied total is " + str(multiply_total))
    # create division conditional
    if enter == "division" or enter == "d":
        divide1 = input("What is the first number you would like to divide? ")
        
        divide2 = input("What is the second number you would like to divide? ")
        
        division_total = int(divide1) / int(divide2)
        
        print("Your final divided total is " + str(division_total))
        print('Your rounded total is ' + str(round(division_total)))
    again = input("Would you like to perform another mathematical calculation? ")
    if again == 'yes' or again == "y":
        continue
    else:
        print('Ok thanks for using the calculator!')
        break
    